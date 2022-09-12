1. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![pbp](/desktop/pbp.png)

Dari client side akan mengirimkan sebuah GET HTTP Request kepada server. Nantinya, server dengan urls.py akan memetakan request ke controller (disini controller nya adalah views) sesuai dengan URL yang seharusnya. Controller yang terdefinisi pada views.py akan me-render file HTML yang ada pada server beserta dengan data yang dibutuhkan. Data yang dirender menjadi sebuah file HTML didapatkan dari database yang berasal dari models.py. 

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Penggunaan sebuah virtual environment sebenarnya tidak diperlukan dalam pembuatan sebuah aplikasi. Jika kita tidak menggunakan virtual environment dalam pembuatan aplikasi, kita bisa saja kekurangan suatu hal yang seharusnya kita siapkan dalam pembuatan aplikasinya. Dengan adanya virtual environment, kita akan sangat terbantu ketika kita membutuhkan dependencies yang berbeda-beda antara project satu dengan yang lainnya yang berjalan pada OS yang sama. 

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pembuatan tugas 2 ini saya mulai dengan melakukan clone dari template repository yang tersedia di GitHub. Setelah itu saya menjalankan perintah dalam virtual environment dan menginstall requirements serta melakukan migrations dan load data yang diperlukan. Setelah itu saya membuat views.py dengan mempersiapkan function yang me-return html file yang telah di render. Saya juga membuat dictionary yang terdiri dari name, student_id, dan catalog yang nantinya akan ditampilkan di aplikasi.

Setelah itu, saya membuat urls.py yang ada pada project_django. urls.py yang ada pada project_django bertujuan untuk memperlihatkan katalog. Oleh karena itu saya perlu mendefinisikan route yang ada di urls.py pada project_django. Kemudian saya tambahkan path yang dibutuhkan agar katalog bisa tampil pada aplikasi.

Setelah membuat views.py, saya melengkapi file katalog.html dengan mengubah fill me menjadi {{name}} untuk me render nama saya di aplikasi. Setelah itu saya tambahkan loop agar bisa semua barang dalam menampilkan katalog

Setelah semuanya benar, saya melakukan deployment dengan cara membuat aplikasi HEROKU dengan mendapatkan API KEY dan menambahkannya pada repository saya dengan cara (repository -> settings -> secrets -> github action). Saya menambahkan 2 secrets yaitu HEROKU_API_KEY dan HEROKU_APP_NAME (HEROKU_API_KEY didapat dari API kita dari HEROKU sedangkan HEROKU_APP_NAME didapat dari nama aplikasi kita)
