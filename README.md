Tugas 2

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

Tugas 3

Peran data delivery dalam implementasi sebuah platform

Konsep aplikasi modern umumnya terpisah antara front-end dan back-end. Selain itu ada pihak ketiga yang turut melengkapi untuk fungsi integrasi, dsb. Data delivery memungkinkan aplikasi untuk melakukan pertukaran data antar-komponen. Hal ini juga mempermudah penggunaan kembali data oleh berbagai client. Diluar hal itu, adanya data delivery memungkinkan aplikasi untuk mengontrol format, versi, dan keamanan akses.Kemudahan lainnya yang diberikan adalah memudahkan automasi, testing, dan integrasi layanan eksternal.

Preferensi metode data delivery dan popularitas JSON

Bagi saya pribadi JSON sedikit lebih unggul dengan readability yang lebih baik dan kecepatannya dalam parsing diberbagai platform. Meski demikian, XML tetap memiliki kelebihannya tersendiri. XML bagus untuk dokumen yang dipenuhi oleh markup, namespace, atribut, atau validasi ketat. Tentu ini cocok untuk B2B system lama.

Adapun popularitas JSON di web API modern didasari oleh beberapa alasan, seperti representasi objek yang natural untuk JavaScript, payload yang lebih kecil, sehingga dapat mendongkrak performa yang lebih optimal. Diluar hal tersebut, JSON memiliki parsing built-in di browser modern. Dari segi keramahan terhadap pemula, JSON jauh lebih mudah untuk di pelajari karena tidak memerlukan namespace atau XPath

Pentingnya fungsi is_valid() pada Django

object.is_valid() penting dalam proses pengembangan aplikasi di Django karena beberapa alasan yakni, memeriksa apakah bound dan semua field memenuhi validasi field-level. Selain itu, fungsi ini juga menjalankan clean_\<field\>() dan clean() pada objek. Fungsi ini juga mengisi object.cleaned_data jika valid, atau form.errors jika tidak. Dalam proses pengembangan, kita membutuhkan is_valid() sebelum menyimpan untuk validasi agar data konsisten dan aman untuk diproses serta mencegah error di DB dan menjaga integritas data.

Peran csrf_token pada pembuatan aplikasi Django

CSRF (Cross-Site Request Forgery) adalash serangan dimana penyerang membuat user yang sudah login mengirim request yang tidak diinginkan ke aplikasi target karena browser mengirim cookie sesi secara otomatis. csrf_token  adalah sebuah token unik pada form yang memastikan request POST berasal dari halaman yang dihasilkan server. Nantinya server akan memeriksa token pada request dan menolak request jika tidak cocok.

Jika kita tidak menambahkan csrf_token, ada beberapa risiko yang harus dihadapi seperti server dapat menerima POST palsu dari situs penyerang.Penyerang bisa membuat HTML/JavaScript di situsnya yang otomatis submit form ke endpoint korban untuk melakukan aksi kejahatan atas nama korban. Oleh karena itu sangat disarankan dalam proses pengembangan untuk selalu meletakkan {% csrf_token %} pada form POST di template Django, kecuali endpoint memang dimaksudkan untuk dipanggil oleh non-browser clients.

Contoh eksploitasi sederhana penetrasi yang dilakukan penyerang adalah membuat halaman tersembunyi yang otomatis mengirim permintaan POST untuk menghapus akun kita saat kita sedang login di aplikasi tersebut.

Step by step implementasi Data Delivery
- Membuat direktori baru pada direktori utama proyek untuk membuat berkas berupa template sadar untuk kerangka web
- Menambahkan direktori yang dibuat kedalam settings.py agar terdeteksi oleh aplikasi
- Membuat berkas baru untuk struktur forms yang berfungsi menerima object baru
- Tambahkan beberapa import kedalam views.py pada direktori aplikasi dan menambahkan beberapa fungsi agar dapat memproses penambahan objek dan pemrosesan data form. Selain itu tambahkan beberapa fungsi juga untuk melihat kerangka kode dalam bentuk JSON ataupun XML
- Ubah bagian tampilan utama agar dapat mengakomodasi perubahan yang terjadi pada kode dan menerima request
- Menambahkan urlpatterns baru pada urls.py agar dapat mengakomodasi perubahan yang dilakukan
- Tambahkan fungsi CRSF pada settings.py proyek

Link screenshot postman: https://drive.google.com/drive/folders/1uq8GAHIe9jSARbpZ5TNCCe8-r8HI-YB9?usp=sharing

Tugas 4

Django AuthenticationForm beserta kelebihan dan kekurangannya

AuthenticationForm adalah Form bawaan di django.contrib.auth.forms untuk menangani proses login . Form ini menyediakan validasi yang akan memanggil authenticate(), pesan error standar, termasuk pengecekan akun inactive dan pola yang aman untuk login.

Kelebihan
- Siap pakai, khususnya dengan fitur validasi input, pesan error, integrasi langsung dengan authenticate() dan sistem auth Django.
- Mendukung penerimaan request di konstruktor yang akan sangat berguna bila backend butuh request.
- Mudah diganti/subclass jika perlu custom checks.

Kekurangan
- Defaultnya mengasumsikan ada field username; untuk custom user model yang menggunakan email sebagai identifier perlu perubahan/subclassing.
- Tidak menyediakan fitur "remember me" / pengaturan expiry session otomatis.
- Bukan solusi siap pakai untuk API.

Perbedaan Autentikasi dan Otorisasi berserta penerapannya di Django

Autentikasi (Authentication): memastikan identitas pengguna umunya melalui proses login yang melibatkan username/password.

Otorisasi (Authorization): menentukan hal yang boleh dilakukan pengguna  seperti permissions, akses resource, dsb.

Implementasi oleh Django

Authentication: fungsi authenticate() + login() yang berguna untuk memasukkan user ke session. request.user menjadi objek User atau dalam kasus anonim, maka AnonymousUser. Django menyediakan views/forms helpers dan backends untuk kustomisasi. 

Authorization: Django menyediakan model permission seperti add/change/delete, user.has_perm('app.codename'), @permission_required, dan Group untuk mengelompokkan permission. Selain itu ada decorator @login_required / mixin LoginRequiredMixin untuk membatasi view hanya untuk pengguna terautentikasi.

Kelebihan dan kekurangan Session dan Cookies

Cookies
- Mudah diproses, dimana browser menyimpan key/value, tersedia di request berikutnya.
- Kapasitas terbatas, mudah diubah oleh client, dan bisa terekspos ke XSS jika tidak HttpOnly.
- Perlu menambahkan mekanisme signing/encryption jika menyimpan data sensitif.

Sessions
- Data session disimpan server-side (DB/cache/file). Client hanya menerima session id.
- Kapasitas lebih besar & dapat menyimpan tipe data Python yang lebih kompleks.
- Butuh penyimpanan server-side (DB/cache).
- Jika menggunakan cookie-based sessions, data ditandatangani tetapi tidak terenkripsi yang artinya bisa dilihat oleh client walau tidak bisa dipalsukan tanpa SECRET_KEY.

Resiko keamanan cookies dan penaggulangannya

Risiko utama
- Adanya serangan XSS yang berupa script yang tidak diinginkan di halaman website, XSS dapat membaca cookie kecuali cookie diberi HttpOnly.
- Peretasan melalui teknik Man-in-the-middle (MITM), dimana cookie tanpa Secure dapat dikirim lewat HTTP yang tidak terenkripsi.
- Fitur CSRF yang mana cookies dikirim otomatis oleh browser sehingga rentan terhadap CSRF jika tidak ada proteksi.
- Rawan terhadap pengintaian client karena cookie ditaruh di client sehingga nilainya dapat dilihat kecuali terenkripsi.

Praktik / mitigasi (Django + web)

Django telah menyediakan berbagai fitur keamanan seperti:
- HttpOnly untuk cookie session dalam mencegah akses JS
- Secure yang hanya akan mengirim lewat HTTPS
- SameSite (Lax/Strict) untuk mengurangi CSRF via cross-site requests.
- CSRF middleware yang bertujuan untuk  mengaktifkan CSRF protection by default untuk POST forms.

Step by step implementation:
- Membuat template yang dibutuhkan seperti file template login dan register
- Mengimport semua library yang dibutuhkan untuk pengembangan
- Membuat form login, register untuk menampung input user
- Membuat fungsi login, register, logout untuk menjalankan proses yang bersangkutan
- Melakukan otorisasi dengan menambahkan dekorator @login_required pada fungsi yang menampilkan halaman utama dan produk
- Menambahkan fungsi cookies pada session pengguna
- Menambahkan path yang bersangkutan dari fungsi di views.py ke urls.py pada direktori aplikasi
- Hubungkan model untuk menanggapi perubahan model yang terjadi selama pengembangan
- Ubah tampilan utama website untuk mengakomodasi fungsi baru yang diterapkan
