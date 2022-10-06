# Lab 4 (Tugas 5)

## Pertanyaan

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
#### Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

- Kelebihan:
1. Perubahan hanya terjadi pada 1 halaman
2. Class dan ID bisa digunakan oleh internal stylesheet
3. Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

- Kekurangan:
1. Performa web jadi lambat, karena CSS yang berbeda-beda dapat mengakibatkan loading ulang setiap berganti halaman website.
2. Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

#### Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.

- Kelebihan:
1. Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
2. Berguna untuk memperbaiki kode dengan cepat.
3. Proses permintaan HTTP yang lebih kecil dan proses _load website_ akan lebih cepat.

- Kekurangan:
1. Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

#### External CSS
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

- Kelebihan:
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
2. Loading website menjadi lebih cepat.
3. File CSS dapat digunakan di beberapa halaman website sekaligus. 

- Kekurangan:
1. Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

2. Jelaskan tag HTML5 yang kamu ketahui.

| Nama Tag | Keterangan / Kegunaan |
|---|---|
| **Basic** |   |
| <!DOCTYPE> | Tag untuk menentukan tipe dokumen |
| <html> | Tag untuk membuat sebuah dokumen HTML |
| <title> | Tag untuk membuat judul dari sebuah halaman |
| <body> | Tag untuk membuat tubuh dari sebuah halaman |
| <h1> to <h6> | Tag untuk membuat heading |
| <p> | Tag untuk membuat paragraf |
| <br> | Memasukan satu baris putus |
| <hr> | Tag untuk membuat perubahan dasar kata didalam isi |
| <!--...--> | Tag untuk membuat komentar |
| **Formatting** |   |
| <acronym> | Tag untuk membuat sebuah akronim (tidak disupport lagi di HTML5) |
| <abbr> | Tag untuk membuat sebuah singkatan |
| <address> | Tag untuk membuat kontak alamat |
| <b> | Tag untuk membuat huruf bercetak tebal |
| <bdi> | Mengisolasi bagian dari teks yang dapat diformat dalam arah yang berbeda dari teks lain di luarnya (tag baru HTML5) |
| <bdo> | Mengganti arah teks |
| <big> | Tag untuk membuat text berhuruf besar (tidak disupport lagi di HTML5) |
| <blockquote> | Tag untuk membuat sebuah bagian text yang dikutip dari sumber lain |
| <center> | Tag untuk membuat jajaran teks menjadi ditengah (tidak disupport lagi di HTML5) |
| <cite> | Tag untuk membuat judul karya |
| <code> | Tag untuk membuat potongan kode komputer di antara text |
| <del> | Tag untuk membuat teks yang telah dihapus dari dokumen |
| <dfn> | Tag untuk membuat sebuah istilah definisi |
| <em> | Tag untuk membuat penekanan teks (tidak disupport lagi di HTML5) |
| <font> | Tag untuk membuat font, warna, dan ukuran untuk teks (tidak disupport lagi di HTML5) |
| <i> | Tag untuk membuat sebuah bagian dari teks yang disesuaikan dengan mood |
| <ins> | Tag untuk membuat teks yang telah dimasukkan ke dalam dokumen |
| <kbd> | Tag untuk membuat input keyboard |
| <mark> | Tag untuk membuat teks yang disorot / ditandai (tag baru HTML5) |
| <meter> | Tag untuk membuat pengukuran skalar |
| <pre> | Tag untuk membuat teks terformat |
| <progress> | Memperlihatkan kemajuan tugas (tag baru HTML5) |
| <q> | Tag untuk membuat kutipan pendek |
| <rp> | Tag untuk membuat apa yang harus ditampilkan di browser yang tidak mendukung penjelasan ruby (tag baru HTML5) |
| <rt> | Tag untuk membuat sebuah anotasi / pengucapan karakter (untuk tipografi Asia Timur) |
| <ruby> | Tag untuk membuat sebuah anotasi ruby (untuk tipografi Asia Timur) (tag baru HTML5) |
| <s> | Tag untuk membuat teks yang tidak lagi benar |
| <samp> | Tag untuk membuat contoh keluaran dari program komputer |
| <small> | Tag untuk membuat teks kecil |
| <strike> | Tag untuk membuat teks yang di coret tengah (tidak disupport lagi di HTML5) |
| <strong> | Tag untuk membuat teks penting |
| <sub> | Tag untuk membuat teks subskrip (seperti dalam penulisan Zat Kimia) |
| <sup> | Tag untuk membuat teks superscripted (seperti dalam penulisan akar kuadrat) |
| <time> | Tag untuk membuat tanggal / waktu (tag baru HTML5) |
| <tt> | Tag untuk membuat teks teletype (tidak disupport lagi di HTML5) |
| <u> | Tag untuk membuat teks yang memiliki Gaya yang berbeda dari teks biasa lainnya |
| <var> | Tag untuk membuat sebuah variabel |
| <wbr> | Tag untuk membuat kemungkinan garis-putus |
| **Forms** |   |
| <form> | Tag untuk membuat sebuah form HTML untuk input pengguna |
| <input> | Tag untuk membuat sebuah kontrol input |
| <textarea> | Tag untuk membuat sebuah kontrol input multibaris (text area) |
| <button> | Tag untuk membuat sebuah tombol yang dapat diklik |
| <select> | Tag untuk membuat sebuah daftar drop-down |
| <optgroup> | Tag untuk membuat sebuah kelompok pilihan yang terkait dalam daftar drop-down |
| <option> | Tag untuk membuat pilihan dalam daftar drop-down |
| <label> | Tag untuk membuat sebuah label untuk sebuah elemen <input> |
| <fieldset> | Grup unsur terkait dalam bentuk |
| <legend> | Tag untuk membuat sebuah caption untuk sebuah elemen <fieldset>, < figure>, atau <details> |
| <datalist> | Menentukan daftar pilihan yang telah ditetapkan untuk kontrol input (tag baru HTML5) |
| <keygen> | Tag untuk membuat key-pair generator kolom input (tag baru HTML5) |
| <output> | Tag untuk membuat hasil penghitungan (tag baru HTML5) |
| **Frames** |   |
| <frame> | Tag untuk membuat sebuah window (bingkai) dalam sebuah frameset (tidak disupport lagi di HTML5) |
| <frameset> | Tag untuk membuat satu set bingkai (tidak disupport lagi di HTML5) |
| <noframes> | Tag untuk membuat sebuah konten alternatif untuk pengguna yang tidak mendukung frame (tidak disupport lagi di HTML5) |
| <iframe> | Tag untuk membuat sebuah bingkai |
| **Images** |   |
| <img> | Tag untuk membuat gambar |
| <map> | Tag untuk membuat gambar-peta |
| <area> | Tag untuk membuat area dalam gambar-peta |
| <canvas> | Digunakan untuk menggambar grafik, melalui scripting (JavaScript ) (tag baru HTML5) |
| <figcaption> | Tag untuk membuat sebuah caption untuk elemen <figure> (tag baru HTML5) |
| <figure> | Menentukan konten mandiri (tag baru HTML5) |
| **Audio/Video** |   |
| <audio> | Tag untuk membuat isi suara (tag baru HTML5) |
| <source> | Tag untuk membuat sumber beberapa media untuk elemen media (<video> dan <audio>) (tag baru HTML5) |
| <track> | Tag untuk membuat trek teks untuk elemen media (<video> dan <audio>) (tag baru HTML5) |
| <video> | Tag untuk membuat sebuah video atau film (tag baru HTML5) |
| **Links** |   |
| <a> | Tag untuk membuat hyperlink |
| <link> | Tag untuk membuat hubungan antara dokumen dan sumber daya eksternal (paling sering digunakan untuk link ke style sheet) |
| <nav> | Tag untuk membuat navigasi link (tag baru HTML5) |
| **Lists** |   |
| <ul> | Tag untuk membuat daftar dengan selain nomor |
| <ol> | Tag untuk membuat daftar dengan nomor |
| <li> | Tag untuk membuat sebuah item daftar |
| <dir> | Tag untuk membuat sebuah daftar direktori (tidak disupport lagi di HTML5) |
| <dl> | Tag untuk membuat sebuah daftar definisi |
| <dt> | Tag untuk membuat istilah (item) dalam daftar definisi |
| <dd> | Defines a description of an item in a definition list |
| <menu> | Tag untuk membuat deskripsi dari item dalam daftar definisi |
| <command> | Tag untuk membuat sebuah tombol perintah bahwa seorang pengguna dapat meminta (tag baru HTML5) |
| **Tables** |   |
| <table> | Tag untuk membuat tabel |
| <caption> | Tag untuk membuat sebuah caption tabel |
| <th> | Tag untuk membuat sebuah sel header tabel |
| <tr> | Tag untuk membuat baris dalam sebuah tabel |
| <td> | Tag untuk membuat sel dalam sebuah tabel |
| <thead> | Mengelompokan isi header dalam sebuah tabel |
| <tbody> | Mengelompokanisi tubuh dalam sebuah tabel |
| <tfoot> | Mengelompokan isi footer dalam sebuah tabel |
| <col> | Menentukan properti kolom untuk setiap kolom dalam elemen <colgroup> |
| <colgroup> | Menentukan kelompok dari satu atau lebih kolom dalam sebuah tabel untuk diformat |
| **Style/Sections** |   |
| <style> | Tag untuk membuat informasi style untuk dokumen |
| <div> | Tag untuk membuat sebuah bagian dalam dokumen |
| <span> | Tag untuk membuat sebuah bagian dalam dokumen |
| <header> | Tag untuk membuat sebuah header untuk dokumen atau bagian (tag baru HTML5) |
| <footer> | Tag untuk membuat footer untuk dokumen atau bagian (tag baru HTML5) |
| <hgroup> | Pengelompokan elemen heading (<h1> sampai <h6>) (tag baru HTML5) |
| <section> | Tag untuk membuat bagian dalam dokumen (tag baru HTML5) |
| <article> | Tag untuk membuat sebuah artikel (tag baru HTML5) |
| <aside> | Tag untuk membuat konten lain selain dari konten halaman (tag baru HTML5) |
| <details> | Tag untuk membuat rincian tambahan yang pengguna dapat lihat atau sembunyikan (tag baru HTML5) |
| <dialog> | Tag untuk membuat sebuah kotak dialog atau jendela (tag baru HTML5) |
| <summary> | Tag untuk membuat sebuah judul terlihat untuk elemen <detil> (tag baru HTML5) |
| **Meta Info** |   |
| <head> | Tag untuk membuat informasi tentang dokumen |
| <meta> | Tag untuk membuat metadata tentang dokumen HTML |
| <base> | Menentukan URL dasar / target untuk semua URL relatif dalam dokumen |
| <basefont> | Menentukan standar warna, ukuran, dan font untuk semua teks dalam dokumen (tidak disupport lagi di HTML5) |
| **Programming** |   |
| <script> | Tag untuk membuat script di sisi klien |
| <noscript> | Tag untuk membuat sebuah konten alternatif bagi pengguna yang tidak mendukung script di sisi klien |
| <applet> | Tag untuk membuat sebuah java applet yang ditanam (tidak disupport lagi di HTML5) |
| <embed> | Tag untuk membuat sebuah wadah untuk aplikasi eksternal (non-HTML) (tag baru HTML5) |
| <object> | Tag untuk membuat sebuah objek yang ditanam |
| <param> | Tag untuk membuat sebuah parameter untuk objek |

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Ada 6 macam selektor di CSS:

1. Selektor Tag
Selektor Tag disbut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag.
Contoh:
```bash
p {
    color: red;
}
```
Artinya: Pilih semua elemen <p> lalu atur warna teksnya menjadi merah.

2. Selektor Class
Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
Contoh:
```bash
.red {
  color: white;
  background: red;
  padding: 5px;
}
```
Kita memiliki selektor class beranam .pink. Nah cara menggunakan selektor ini di HTML adalah dengan menambahkan atribut class di dalamnya.

3. Selektor ID
Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja.
Selektor ID ditandai dengan tanda pagar (#) di depannya.
Contoh:
```bash
#header {
    background: teal;
    color: white;
    height: 100px;
    padding: 50px;
}
```

4. Selektor Atribut
Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
Contoh selektor Atribut:
```bash
input[type=text] {
    background: none;
    color: cyan;
    padding: 10px;
    border: 1px solid cyan;
}
```
Artinya kita akan memilih semua elemen <input> yang memiliki atribut type='text'.

5. Selektor Universal
Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.
Contoh:
```bash
* {
    border: 1px solid grey;
}
```
Artinya semua elemen akan memiliki garis solid dengan ukuran 1px dan berwarna grey.
Selektor universal bisanya digunakan untuk me-reset CSS. Pada halaman HTML, ada beberapa CSS bawaan browser seperti padding dan margin pada elemen tertentu. Reset bertujuan untuk menghilangkan padding dan margin tersebut.

6. Selektor Pseudo
Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.
Ada dua macam pseudo selektor:
- pseudo-class selektor untuk state elemen;
Pseudo-class adalah selektor untuk memilih state pada elemen.
Contohnya seperti elemen saat diklik, saat fokus, saat disentuh, dan lain sebagainya.
Contoh:
```bash
a:hover {
  color: green;
}
```
Kita akan memberikan warna hijau pada elemen <a> saat dia di-hover atau disentuh pointer.

- pseudo-element selektor untuk elemen semu di HTML.
Contoh:
```bash
p::first-line {
  color: magenta;
}
```
Selektor pseudo-element menggunakan tanda titik dua ganda (::) sedangkan pseudo-class pakai satu titik dua (:).

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Melakukan kustomisasi template HTML, menggunakan _CSS framework_ yaitu Bootstrap. Dilakukan dengan mengimpor link Bootstrap ke dalam template HTML.

- Untuk mengkostumisasi halaman login dan register diperlukan pembuatan `forms.py` agar dapat mengubah mengubah `UserCreationForm` dan `AuthenticationForm` menjadi seperti yang diinginkan.

- Kustomisasi halaman todo list menggunakan card dari Bootstrap dengan penambahan sub-bagian pada template HTML.
Kode penambahan card pada `todolist.html`:
```bash
<div class="card text-white bg-dark mb-3" style="max-width: 18rem">
    <div class="card-header">{{todo.date}}</div>
        <div class="card-body">
            <h5 class="card-title">{{todo.title}}</h5>
            <p class="card-text">{{todo.description}}</p>
        </div>
    </div>
```

- Membuat halaman menjadi responsive dengan mengimpor JS Bootstrap pada bagian bawah body template HTML. Dapat terlihat pada tombol toggle navbar yang menjadi _collapsing_ saat berada pada layar atau resolusi yang berbeda dan perangkat yang berbeda.