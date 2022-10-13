<h3> Link Menuju HEROKU : http://tugaspbpkedua.herokuapp.com/todolist/<h3>

## Apa kegunaan {% csrf_token %} pada elemen ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ?

CSRF token berguna untuk mencegah serangan CSRF. Ddengan adanya CSRF token, serangan CSRF semakin sulit terjadi dengan membuat penyerang tidak mungkin membuat HTTP request yang sepenuhnya valid yang cocok untuk diumpankan ke korban.

Kita tetap bisa menjalankan website kita tanpa menggunakan CSRF token. Namun, kita akan rentan terkena serangan CSRF. Sehingga, penggunaan CSRF Token disarankan untuk alasan keamanan.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Kita bisa saja membuat elemen `<form>` tanpa menggunakan `{{ form.as_table }}`. Dengan memanfaatkan elemen `<table>`, kita bisa generate table untuk menjadi dasar dari form kita. Kemudian kita bisa memanfaatkan elemen `<tr>` dan `<td>` untuk memasukkan data ke baris. Untuk memasukkan input, kita bisa memanfaatkan elemen `<input>`. Lalu, kita bisa memanfaatkan sebuah button untuk melakukan submission dengan mengubah atribut `type=` menjadi `submit`.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

User akan melakukan pengisian formulir yang ada pada halaman HTML yang disajikan. Setelah user memencet tombol submit, akan dilakukan HTTP Request dan data akan dikirimkan ke server. Setelah itu akan dilakukan pengecekan validitas mengenai request tersebut. Jika request tersebut valid, views yang ada pada `views.py` akan disesuaikan untuk dilakukan tampilan. Setelah itu, views akan mengembalikan HTTP Response dan halaman HTML yang sesuai kepada user.

## Implementasi Checklist

1. Saya menjalankan perintah `python manage.py startapp todolist` pada terminal
2. Saya menambahkan path `path('todolist/', include('todolist.urls'))` pada `urls.py` yang ada pada folder `project_django`, kemudian saya membuat fungsi show_todolist pada `views.py`
3. Kemudian membuat models dengan field yang sesuai dengan perintah di `models.py`
4. Lalu menambahkan fungsi login, logout dan register serta html dari login dan register yaitu `login.html` dan `register.html`.
5. Setelah itu, menambahkan page html dari todolist yaitu `todolist.html` yang berfungsi untuk menampilkan To Do List yang sudah dibuat beserta elemen yang dibutuhkan (seperti button create task, logout)
6. Setelah membuat button `Tambah Task` yang ada di `todolist.html`, buat page baru yaitu `create-task.html` untuk mengarahkan user ke page untuk menambah task baru. Sebelumnya, jangan lupa untuk menambahkan fungsi pada `views.py` untuk menambah task baru.
7. Menambahkan fungsi untuk menampilkan elemen yang mengindikasikan jika task tersebut sudah dijalankan atau belum pada `views.py`
8. Membuat elemen checklist yang menandakan bahwa task tersebut telah selesai di `todolist.html`
9. Setelah aplikasi bisa melakukan register, login, create task dan logout, lakukan routing agar bisa terhubung antar page
10. Melakuakan deployment ke Heroku.

<h3> Tugas 5 </h3>

## Perbedaan Inline, Internal dan External CSS serta kelebihan dan kekurangan masing-masing

Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan dituliskan di bagian header file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman yang lain. Sehingga, jika kita ingin setiap halaman pada website kita tampilannya berbeda, Internal CSS sangat cocok digunakan.

Kelebihan Internal CSS :

- Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
- Kita tidak perlu upload beberapa file karena HTML dan CSS berada dalam satu file.
- Class dan ID bisa digunakan oleh internal stylesheet

Kekurangan Internal CSS :

- Tidak efisien apabila kita ingin menggunakan CSS yang sama dalam beberapa file.
- Performa website akan lebih lemot karena CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali kita ganti halaman website.

External CSS adalah kode CSS yang ditulis terpisah dengan kode HTML. External CSS ditulis di sebuah file dengan extension .css. File external biasanya ditulis setelah bagian `<head>` pada halaman.

Kelebihan External CSS :

- Ukuran file HTMl akan lebih kecil dan kode HTML akan terlihat lebih rapi.
- Loading website menjadi lebih cepat.
- File CSS dapat digunakan di beberapa halaman website sekaligus.

Kekurangan External CSS :

- Karena koneksi internet yang lambat, halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki attribute style, lalu disitulah inline CSS ditulis. Cara ini sebenarnya kurang efisien karena setiap tag HTML harus diberikan style masing-masing. Inline CSS digunakan hanya untuk mengatur satu elemen saja.

Kelebihan Inline CSS :

- Sangat membantu ketikakita hanya ingin menguji dan melihat perubahan pada satu elemen.
- Berguna untuk memperbaiki kode dengan cepat.
- Proses HTTP request lebih kecil dan proses load website akan lebih cepat.

Kekurangan Inline CSS :

- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

## Tag HTML5

Beberapa tag HTML 5 yang saya ketahui sebagai berikut :

1. `<a>` berguna untuk mendefinsikan hyperlink
2. `<b>` berguna untuk menampilkan text dengan style bold
3. `<br>` berguna untuk menghasilkan single line break
4. `<button>` berguna untuk membuat button
5. `<td>` berguna untuk mendefiniskan cell di dalam tabel
6. `<th>` berguna untuk mendefiniskan header cell di dalam tabel
7. `<title>` berguna untuk mendefinisikan title dokumen
8. `<tr>` berguna untuk mendefinisikan row cell didalam tabel
9. `<ul>` berguna untuk mendefinsikan unordered list
10. `<table>` berguna untuk mendefinsikan data dalam tabel

## Tipe tipe CSS Selector

Beberapa CSS Selector :

1. CSS element selector
   Element selector memilih HTML elements berdasarkan nama element

```
...
p {
  text-align: center;
  color: red;
}
...
```

2. CSS id selector
   Id selector menggunakan attribute id dari sebuah element HTML untuk memilih specific element. Id sebuah element unik, sehingga id selector berguna untuk memilih 1 element yang unik

```
...
#para1 {
  text-align: center;
  color: red;
}
...
```

3. CSS class selector
   Class selector memilih HTMl element dengan class attribute yang spesifik. UNtuk memilih element dengan specific class, kita gunakan titik(.) lalu diikuti dengan nama class

```
...
.center {
  text-align: center;
  color: red;
}
...
```

4. CSS Universal selector
   Universal selector memilih seluruh HTML elements di dalam halaman

```
...
* {
  text-align: center;
  color: blue;
}
...
```

5. CSS Grouping selector
   Grouping selector memilih semua HTML elements dengan definisi style yang sama

```
...
h1 {
  text-align: center;
  color: red;
}

h2 {
  text-align: center;
  color: red;
}

p {
  text-align: center;
  color: red;
}
...
```

## Implementasi

1. Menambahkan beberapa hal agar website bisa menggunakan bootstrap
2. Mengaplikasikan card ke dalam page `register`, `create-task`, `login` dan 1 card per task untuk `todolist`
3. Styling menggunakan inline CSS, sesuai dengan yang diinginkan
4. Memanfaatkan framework bootstrap agar bisa memberi warna pada card yang diinginkan dengan cara memberikan class pada tiap tag `<div>`
5. Lakukan hal yang sama. Dengan memanfaatkan bootstrap, kita bisa mengostumisasi button yang ada pada halaman
6. Atur width, margin dan sizing
7. Commit, dan push

<h3> Tugas 6 </h3>

## Perbedaan antara asynchronous programming dan synchronous programming

Synchronous adalah proses jalannya program secara sequential, maksud dari sequential adalah berdasarkan antrian eksekusi program. Sedangkan asynchronous, proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous.

## Arti dari event driven programming

Event driven programming adalah paradigma programming dimana eksekusi program ditentukan oleh user events, sensor outputs ataupun messageyang di passing dari program yang lain. Pada program ini terdapat button yang jika ditekan akan melakukan function tertentu, contohnya yaitu "Create Task"

## Asynchronous Programming di AJAX

1. Tamhahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` pada header
2. Tambahkan tag `<script>` pada body
3. Tuliskan JQuery syntax didalam script untuk melakukan method POST, DELETE, dan lain-lain
4. AJAX akan mendengar event listener yang kita tuliskan dalam script untuk menerapkan action yang kita inginkan
5. Action yang dilakukan akan diproses secara asynchronous didalam server
6. Data akan ditampilkan di page kita tanpa kita harus refresh

## Implementasi

1. Buat function `show_json` di `views.py`
2. Edit `show_todolist` didalam `views.py` agar sesuai dengan ketentuan
3. Tambahkan Script AJAX dalam `base.html` bagian header
4. Tambahkan function `add task` pada `views.py` untuk post data menggunakan AJAX
5. Tambahkan function GET pada `todolist.html`
6. Buat modal untuk menambahkan task baru
7. Tambahkan function POST pada `todolist.html`
