Link deployment: https://jefferson-tirza-footballshop.pbp.cs.ui.ac.id/

Step by step pengerjaan tugas:
- Buatlah sebuah direktori baru untuk membuat proyek Django baru, setelah itu, inisialisasi virtual environment dan aktifkan enviroment tersebut.
- Buatlah sebuah proyek baru dengan perintah 'django-admin startproject [nama proyek]'
- Lalu masuk ke direktori proyek dan buatlah aplikasi main dengan perintah 'python manage.py startapp'
- Setelah main sudah dibuat, tambahkan main kedalam INSTALLED_APPS pada berkas settings.py agar dapat dikenali oleh Django.
- Buatlah sebuah template tampilan dengan membuat file html pada direktori aplikasi yang dibuat
- Modifikasi berkas models.py pada direktori aplikasi dengan menambahkan/mengubah atribut pada model hingga sesuai dengan ketentuan
- Lakukan migrasi model dengan perintah 'python manage.py makemigrations' lalu 'python manage.py migrate' untuk membuat tabel database.
- Implementasikan MVT dengan memodifikasi berkas views.py pada direktori aplikasi dan tambahkan fungsi render dan fungsi untuk menampilkan halaman dari web yang dibuat.
- Lakukan konfigurasi routing pada urls.py di direktori aplikasi dengan mengimport fungsi, menambahkan variable nama aplikasi dan pattern dari url.
- Lanjutkan konfigurasi dengan memodifikasi berkas urls.py pada berkas proyek dan tambahkan include pada import serta masukkan url aplikasi kepada list urlpatterns.
- Lakukan deployment di pws, dengan membuat proyek baru dan menghubungkan proyek dengan server.

Peran settings.py dalam proyek Django
- Menyimpan semua konfigurasi global proyek.
- Mengatur koneksi database.
- Menentukan daftar aplikasi yang aktif melalui INSTALLED_APPS.
- Mengatur lokasi template, static files, dan media files.
- Menyimpan kunci keamanan dan pengaturan debug.

Cara kerja migrasi database di Django
- Saat kita membuat atau mengubah model, Django perlu menyinkronkan ke database.
- Perintah 'makemigrations' menghasilkan file migrasi yang berisi instruksi perubahan tabel sedangkan perintah 'migrate' mengeksekusi file migrasi ke database sehingga struktur tabel sesuai dengan model.

Bagan request client: https://www.canva.com/design/DAGyaFcGcbo/OJVS_t3e_4zRUQecP4eZDg/edit?utm_content=DAGyaFcGcbo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Penjelasan

Client mengirim request ke server, lalu urls.py memetakan request ke fungsi yang sesuai di views.py. Nantinya, views.py akan menjalankan perintah, jika perlu mengambil atau menyimpan data maka memanggil models.py. Disini models.py berhubungan dengan database. Setelah data diproses, views.py mengirimkannya ke template HTML. Template HTML akan dirender menjadi response. Response dikirim kembali ke client.

Alasan Django jadi framework awal pembelajaran

Menurut saya, alasannya cukup sederhana. Framework Django memakai bahasa Python yang sintaksnya mudah dibaca. Selain itu, Django sudah cukup lengkap dengan adanya Object Relational Mapping (ORM), template engine, dan admin panel. Django juga berfokus pada pola arsitektur MVT (Model View Template) sehingga memudahkan pengguna untuk belajar arsitektur website.