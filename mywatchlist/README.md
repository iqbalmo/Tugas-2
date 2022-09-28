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