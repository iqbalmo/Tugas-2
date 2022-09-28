# Lab 1 (Tugas 2)

## Pertanyaan

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

<img src="img/Django Response Cycle by hackr.io.png" width="1000">

Kaitan antara satu sama lain adalah tugas masing-masing dalam menjalankan suatu project Django. Model berfungsi sebagai basis data yang menyimpan suatu kelas dan menjadi sebuah cetakan untuk memetakan data. Views bertugas sebagai fungsi logika untuk memunculkan berkas html yang telah dibuat. Lalu urls berfungsi untuk melakukan routing/menyambungkan antara bagian satu dengan yang lain sehingga bagian yang telah dihubungkan dapat ditampilkan.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment dalam segi kebahasaan memiliki arti yaitu lingkungan maya. Sesuai dengan artinya, virtual environment digunakan untuk membuat lingkungan virtual python yang terisolasi dari sistem operasi secara keseluruhan, sehingga tidak akan ada konflik antar project yang sedang dikembangjkan. Penggunaan virtual environment adalah untuk menyeragamkan penggunaan versi-versi library yang digunakan pada suatu project, karena pada setiap project memiliki kebutuhan library yang berbeda beda dan versi yang bermacam macam.

Lalu, bagaimana jika tidak menggunakan virtual environment? Bisa, tetapi akan sulit untuk diaplikasikan ke banyak project sekaligus, pemenuhan requirements satu project akan menyulitkan pemenuhan requirements di project lain, seperti penggunaan versi library yang berbeda. Apabila versi library yang digunakan tidak sesuai dengan kebutuhan maka akan memunculkan error. Maka sebaiknya setiap project Django memiliki virtual environmentnya masing-masing.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

- Poin 1 = Diimplementasikan dengan membuat fungsi show_katalog pada views yang berfungsi untuk mengambil data dari model dan mengembalikannya pada HTML.

```bash
  def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_katalog,
    'nama': 'Mochammad Iqbal',
    'npm': '2006531056'
    }
    return render(request, "katalog.html", context)
```

- Poin 2 = Routing pada views dilakukan dengan membuat urls.py untuk memetakan fungsi yang telah dibuat dan juga mendaftarkannya pada urls.py utama agar dapat ditampilkan.

Kode pada katalog\urls.py
```bash
  urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

Kode pada project_django\urls.py
```bash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```

- Poin 3 = Pemetaan data dilakukan dengan iterasi terhadap variabel list_barang yang terdapat pada templates\katalog.html. Pemanggilan juga dilakukan dengan memanggil atribut spesifik objek dari dalam kontainer.

```bash
{% for barang in list_barang %}
      <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.item_url}}</th>
      </tr>
    {% endfor %}
```

- Poin 4 = Deployment dilakukan dengan pembuatan app di Heroku, app ini bernama cataloglab yang pengimplementasian tugas-2 ini tersedia pada https://cataloglab.herokuapp.com/katalog. Prosedur deployment dilakukan dengan membuat app baru di heroku, lalu memasukkan nama app dan API key pada repository secrets di github. `Settings > Secrets - Action > New repository secret` dan mengisikan HEROKU_API_KEY dan HEROKU_APP_NAME.