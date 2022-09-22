# Tugas

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

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

# Lab 2 (Tugas 3)

## Pertanyaan

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
- JSON adalah singkatan dari JavaScript Object Notation merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Sederhananya, JSON adalah bagian dari JavaScript yang digunakan untuk menyimpan dan mentransfer data. Ekstensi file JSON adalah .json.

- XML adalah singkatan dari Extensive Markup Language merupakan sebuah markup language yang dirancang untuk menyimpan dan mengantarkan data. Meskipun memiliki fungsi serupa, JSON dan XML merupakan dua hal yang berbeda. Ekstensi file JSON adalah .json, sementara file XML diakhiri dengan .xml.

- HTML adalah singkatan dari Hypertext Markup Language merupakan sebuah bahasa markup yang digunakan untuk membuat halaman website. Isinya terdiri dari berbagai kode yang dapat menyusun struktur suatu website. HTML terdiri dari kombinasi teks dan simbol yang disimpan dalam sebuah file. Dalam membuat file HTML, terdapat standar atau format khusus yang harus diikuti. Format tersebut telah tertuang dalam standar kode internasional atau ASCII (American Standard Code for Information Interchange). 

| JSON | XML | HTML |
|---|---|---|
| JSON adalah format pertukaran data yang ringan | XML dirancang untuk membawa data, bukan untuk  menampilkan data | HTML dirancang untuk menampilkan data |
| JSON adalah Notasi Objek Javascript | XML adalah bahasa markup | HTML adalah bahasa markup |
| JSON berdasarkan bahasa Javascript | XML berasal dari SMGL (Standard Generalized  Markup Language) | HTML berasal dari SMGL (Standart Generalized Markup Language |
| JSON berorientasi pada data | XML berorientasi pada dokumen | HTML berorientasi pada penyajian data |
| JSON mendukung penggunaan array | XML tidak mendukung penggunaan array | HTML memiliki tag terbatas |
| Lebih mudah dibaca dan dipahami | Lebih rumit untuk dibaca dan dipahami | Lebih mudah dibaca dan dipahami |
| JSON tidak menggunakan tag | XML menggunakan tag pada awal dan akhir | HTML tersusun dari tag khusus agar dapat berfungsi |
| JSON tidak mendukung penggunaan comment | XML mendukung penggunaan comment | HTML mendukung penggunaan comment |
| Ukuran file JSON cenderung lebih kecil | Ukuran file XML cenderung lebih besar | Ukuran file HTML cenderung kecil |
| JSON hanya mendukung UTF-8 encoding | XML mendukung berbagai encoding | HTML memiliki encoding default UTF-8 |
| File JSON memiliki ekstensi file .json | File XML memiliki ekstensi file .xml | File HTML memiliki ekstensi file .html |


2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam sebuah platform diperlukan komunikasi data yang baik sehingga data yang akan diantarkan dapat sesuai dengan tujuan awal implementasinya, fungsi utamanya adalah untuk mengefisiensikan sebuah pengiriman data dalam jumlah yang besar tanpa suatu kesalahan. Selain itu data delivery juga berfungsi untuk menyampaikan informasi yang terdapat pada suatu platform kepada user atau pengunjung mengenai data yang ada di dalamnya, dalam hal ini juga dapat berbentuk tampilan teks, gambar, dan lain lain. Data delivery sangat diperlukan untuk mengerti tujuan dari sebuah platform, untuk apa dibuat dan untuk apa aplikasinya.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat suatu aplikasi baru bernama mywatchlist dengan perintah `python manage.py startapp mywatchlist`

- Melakukan routing pada urls.py agar mywatchlist dapat diakses

- Membuat class MyWatchlist pada models.py dengan atribut watched, title,, rating, release_date, review dan mengisikan data pada `fixtures/initial_watchlist_data.json`

- Menyajikan data dalam bentuk HTML hanya perlu mengcopy sajian data awal pada `mywatchlist/` menjadi routing ke `mywatchlist/html`

- Menyajikan data dalam bentuk XML dengan menggunakan fungsi pada views dan menambahkan path routing ke `mywatchlist/xml`

```bash
def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

- Menyajikan data dalam bentuk XML dengan menggunakan fungsi pada views dan menambahkan path routing ke `mywatchlist/json`

```bash
def show_mywatchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- Deployment dilakukan dengan pembuatan app di Heroku, app ini bernama cataloglab yang pengimplementasian tugas-3 ini tersedia pada https://cataloglab.herokuapp.com/mywatchlist. Prosedur deployment dilakukan dengan membuat app baru di heroku, lalu memasukkan nama app dan API key pada repository secrets di github. `Settings > Secrets - Action > New repository secret` dan mengisikan HEROKU_API_KEY dan HEROKU_APP_NAME.

#### Screenshot Postman

1. Screenshot HTML

<img src="img/Screenshot HTML.png" width="500">

2. Screenshot XML

<img src="img/Screenshot XML.png" width="500">

3. Screenshot JSON

<img src="img/Screenshot JSON.png" width="500">

Ketiganya menunjukkan status `Status: 200 OK`