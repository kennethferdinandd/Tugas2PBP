<h1>Link menuju Heroku : https://tugaspbpkedua.herokuapp.com/ </h1>

<h1> Perbedaan HTML, JSON dan XML </h1>

- JSON (JavaScript Object Notation) biasanya menampilkan data dalam bentuk key dan value. JSON biasa digunakan dalam pertukaran data dan dapat dibilang pertukaran data berlangsung dengan cepat karena data disimpan dalam bentuk array. JSON dibuat dengan dasar JavaScript.
- HTML (HyperText Markup Language) merupakan salah satu markup language yang biasanya digunakan untuk penyajian data dalam website-website. 
- XML (Extensible Markup Language) merupakan salah satu markup language lainnya yang biasa digunakan untuk mempermudah proses pengiriman data antar server. XML menyimpan data dalam format teks yang kurang lebih mirip dengan HTML.

<h1> Mengapa diperlukan data delivery dalam mengimplementasikan sebuah platform </h1>

Dalam sebuah platform, terjadi biasanya kita melihat sekumpulan data. Data tersebut bisa berasal dari mana saja, dan pastinya terjadi pertukaran data antara clients dan server. Dalam proses pertukaran ini, tentunya ada format yang telah disetujui untuk mempermudah proses pengiriman data. Biasanya format nya antara JSON, HTML dan juga XML.

<h1> Implementasi </h1> 

1. Dalam memulai aplikasi mywatchlist, saya menggunakan command `python manage.py startapp mywatchlist` pada directory yang diinginkan
2. Setelah itu, saya menambahkan `path('mywatchlist/', include('mywatchlist.urls')),` pada file urls.py yang ada di urlpatterns yang berada dalam folder django_project 
3. Lalu saya menambahkan `urlpatterns = [ ..., path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), ... ]` pada urls.py yang ada pada file mywatchlist saya
4. Kemudian saya membuat models.py yang berada di folder mywatchlist dengan model bernama MyWatchlist dengan data fields watched, title, rating, release_date, dan review
5. Setelah itu, saya jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi agar model dapat terbuat pada database.
6. Kemudian saya membuat folder yang bernama fixtures didalam mywatchlist untuk membuat file bernama initial_mywatchlist_data.json yang berisi data yang akan digunakan
7. Setelah itu saya jalankan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data tersebut ke local saya
8. Lalu saya menambahkan fungsi yang dibutuhkan pada file views.py
9. Tidak lupa untuk membuat folder templates yang berisi mywatchlist.html untuk mapping data yang ada pada fungsi views untuk menampilkan pada page HTML
10. Karena kita perlu data dalam bentuk XML dan JSON, buat fungsi untuk menampilkan data dalam bentuk XML dan JSON pada views.py
11. Pada file tests.py, buat testing 
12. Ubah file settings.py agar bisa menjalankan tests.py
13. Jalankan perintah `python manage.py loaddata initial_mywatchlist_data.json` dan `python manage.py test`
14. Ubah procfile agar aplikasi dapat berjalan

<h1> Postman </h1>

<h2> HTML </h2>
![HTML](/assets/html.jpg)

<h2> XML </h2>
![XML](/assets/xml.jpg)

<h2> JSON </h2>
![JSON](/assets/json.jpg)
