# Lab 3 (Tugas 4)

## Pertanyaan

1. Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

CSRF merupakan singkatan dari Cross Site Request Forgery. Token CSRF adalah token acak yang digunakan untuk mencegah serangan CSRF. Token harus unik per sesi pengguna dan harus bernilai sangat acak agar sulit ditebak. Aplikasi yang aman dari CSRF memberikan token CSRF unik untuk setiap sesi pengguna. 

Yang akan terjadi ketika tidak ada `{% csrf_token %}` adalah akan muncul error Forbidden (403) dengan keterangan `CSRF verification failed. Request aborted.` alasan error ini adalah tidak adanya CSRF token. Maka dapat diketahui bahwa jika tidak ada potongan kode token csrf akan terjadi error sampai ditambahkannya token csrf.

2. Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Ya, bisa. Dalam pembuatan `<form>` secara manual diperlukan field-field input yang mewakili variabel yang terdapat pada model. 
Contoh dalam proyek ini adalah seperti berikut (secara default):
```bash
    <form>
        <input type="text">
        <textarea name="" id="" cols="30" rows="10"></textarea>
    </form>
```

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.

Form yang telah disubmit berupa judul dan deskripsi task, akan diterima dalam bentuk request.POST, yang mana akan dibentuk kembali ke dalam model Task dengan parameter semula, yaitu user, title, description, dan date. Masing-masing value tersebut telah disimpan dalam variabel masing masing. Setelah variabel dengan value Task() telah dibuat, digunakan command .save() untuk menyimpan value tersebut ke dalam Django database. Setelah itu dari user yang telah login akan diambil data todolistnya dan ditampilkan dalam bentuk tabel dengan mengiterasi nilai-nilai yang ada di dalamnya.

Berikut potongan kode fungsi create_task pada views.py:
```bash
    def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        date = datetime.date.today()

        new_task = Task(user=user, date=date, title=title, description=description)
        new_task.save()
    context = {}
    return render(request, 'create_task.html', context)
```

Berikut potongan kode fungsi show_todolist pada views.py:
```bash
    def show_todolist(request):
    todo = Task.objects.filter(user=request.user)
    context = {
        'todo_list': todo
    }
    return render(request, "todolist.html", context)
```

4. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.

- Membuat suatu aplikasi baru bernama `todolist` di proyek tugas Django yang sudah digunakan sebelumnya dengan menggunakan `python manage.py startapp todolist`.

- Menambahkan _path_ `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist dengan mendaftakan apps ke INSTALLED_APPS dan melakukan routing pada urls.py di project_django dan membuat file urls.py di dalam folder todolist agar todolist dapat diakses.

- Membuat sebuah model `Task` dengan atribut user, title, description, dan date, yang mana potongan kodenya adalah sebagai berikut:

```bash
    class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length = 30)
    title = models.CharField(max_length = 200)
    description = models.TextField()
```

- Mengimplementasikan form registrasi, _login_, dan _logout_ agar pengguna dapat menggunakan `todolist` dengan baik. Diimplementasikan dengan pembuatan lembar html baru untuk login dan register. Dilakukan pengimplementasi logika juga dalam views.py untuk register, login, dan logout.

- Membuat halaman utama `todolist` yang memuat _username_ pengguna, tombol `Tambah Task Baru`, tombol _logout_, serta tabel berisi tanggal pembuatan _task_, judul _task_, dan deskripsi _task_. Pengambilan _username_ pengguna dengan menggunakan `user.get_username` pada template html. Tombol penambahan task baru dengan menambahkan button yang diarahkan ke url `/create-task`, tombol logout yang diarahkan ke url `/logout`, dan tabel yang menjadi hasil iterasi dari _database_ user di input todolist.

- Membuat halaman form untuk pembuatan _task_. Data yang perlu dimasukkan pengguna hanyalah judul _task_ dan deskripsi _task_. Diimplementasikan dengan pembuatan form secara manual dengan elemen `<form>`.

- Membuat _routing_ sehingga beberapa fungsi dapat diakses melalui URL. _Routing_ telah dilakukan di awal bersamaan dengan pengimplementasian fungsi pada views.py agar dapat saling bersinergi satu sama lain dari awal.

- Melakukan _deployment_ ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. _Deployment_ dilakukan dengan pembuatan app di Heroku, app ini bernama cataloglab yang pengimplementasian tugas-3 ini tersedia pada https://cataloglab.herokuapp.com/todolist. Prosedur deployment dilakukan dengan membuat app baru di heroku, lalu memasukkan nama app dan API key pada repository secrets di github. `Settings > Secrets - Action > New repository secret` dan mengisikan HEROKU_API_KEY dan HEROKU_APP_NAME.