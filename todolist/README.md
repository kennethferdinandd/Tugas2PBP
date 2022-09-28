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
