## Tugas 2

**Link deployment:** https://jefferson-tirza-footballshop.pbp.cs.ui.ac.id/

**Step by step pengerjaan tugas:**
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

**Peran settings.py dalam proyek Django**
- Menyimpan semua konfigurasi global proyek.
- Mengatur koneksi database.
- Menentukan daftar aplikasi yang aktif melalui INSTALLED_APPS.
- Mengatur lokasi template, static files, dan media files.
- Menyimpan kunci keamanan dan pengaturan debug.

**Cara kerja migrasi database di Django**
- Saat kita membuat atau mengubah model, Django perlu menyinkronkan ke database.
- Perintah 'makemigrations' menghasilkan file migrasi yang berisi instruksi perubahan tabel sedangkan perintah 'migrate' mengeksekusi file migrasi ke database sehingga struktur tabel sesuai dengan model.

**Bagan request client:** https://www.canva.com/design/DAGyaFcGcbo/OJVS_t3e_4zRUQecP4eZDg/edit?utm_content=DAGyaFcGcbo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

**Penjelasan Bagan**

Client mengirim request ke server, lalu urls.py memetakan request ke fungsi yang sesuai di views.py. Nantinya, views.py akan menjalankan perintah, jika perlu mengambil atau menyimpan data maka memanggil models.py. Disini models.py berhubungan dengan database. Setelah data diproses, views.py mengirimkannya ke template HTML. Template HTML akan dirender menjadi response. Response dikirim kembali ke client.

**Alasan Django jadi framework awal pembelajaran**

Menurut saya, alasannya cukup sederhana. Framework Django memakai bahasa Python yang sintaksnya mudah dibaca. Selain itu, Django sudah cukup lengkap dengan adanya Object Relational Mapping (ORM), template engine, dan admin panel. Django juga berfokus pada pola arsitektur MVT (Model View Template) sehingga memudahkan pengguna untuk belajar arsitektur website.

## Tugas 3

**Peran data delivery dalam implementasi sebuah platform**

Konsep aplikasi modern umumnya terpisah antara front-end dan back-end. Selain itu ada pihak ketiga yang turut melengkapi untuk fungsi integrasi, dsb. Data delivery memungkinkan aplikasi untuk melakukan pertukaran data antar-komponen. Hal ini juga mempermudah penggunaan kembali data oleh berbagai client. Diluar hal itu, adanya data delivery memungkinkan aplikasi untuk mengontrol format, versi, dan keamanan akses.Kemudahan lainnya yang diberikan adalah memudahkan automasi, testing, dan integrasi layanan eksternal.

**Preferensi metode data delivery dan popularitas JSON**

Bagi saya pribadi JSON sedikit lebih unggul dengan readability yang lebih baik dan kecepatannya dalam parsing diberbagai platform. Meski demikian, XML tetap memiliki kelebihannya tersendiri. XML bagus untuk dokumen yang dipenuhi oleh markup, namespace, atribut, atau validasi ketat. Tentu ini cocok untuk B2B system lama.

Adapun popularitas JSON di web API modern didasari oleh beberapa alasan, seperti representasi objek yang natural untuk JavaScript, payload yang lebih kecil, sehingga dapat mendongkrak performa yang lebih optimal. Diluar hal tersebut, JSON memiliki parsing built-in di browser modern. Dari segi keramahan terhadap pemula, JSON jauh lebih mudah untuk di pelajari karena tidak memerlukan namespace atau XPath

**Pentingnya fungsi `is_valid()` pada Django**

`object.is_valid()` penting dalam proses pengembangan aplikasi di Django karena beberapa alasan yakni, memeriksa apakah bound dan semua field memenuhi validasi field-level. Selain itu, fungsi ini juga menjalankan `clean_\<field>()` dan `clean()` pada objek. Fungsi ini juga mengisi object.cleaned_data jika valid, atau form.errors jika tidak. Dalam proses pengembangan, kita membutuhkan `is_valid()` sebelum menyimpan untuk validasi agar data konsisten dan aman untuk diproses serta mencegah error di DB dan menjaga integritas data.

**Peran csrf_token pada pembuatan aplikasi Django**

CSRF (Cross-Site Request Forgery) adalash serangan dimana penyerang membuat user yang sudah login mengirim request yang tidak diinginkan ke aplikasi target karena browser mengirim cookie sesi secara otomatis. csrf_token  adalah sebuah token unik pada form yang memastikan request POST berasal dari halaman yang dihasilkan server. Nantinya server akan memeriksa token pada request dan menolak request jika tidak cocok.

Jika kita tidak menambahkan csrf_token, ada beberapa risiko yang harus dihadapi seperti server dapat menerima POST palsu dari situs penyerang.Penyerang bisa membuat HTML/JavaScript di situsnya yang otomatis submit form ke endpoint korban untuk melakukan aksi kejahatan atas nama korban. Oleh karena itu sangat disarankan dalam proses pengembangan untuk selalu meletakkan {% csrf_token %} pada form POST di template Django, kecuali endpoint memang dimaksudkan untuk dipanggil oleh non-browser clients.

Contoh eksploitasi sederhana penetrasi yang dilakukan penyerang adalah membuat halaman tersembunyi yang otomatis mengirim permintaan POST untuk menghapus akun kita saat kita sedang login di aplikasi tersebut.

**Step by step implementasi Data Delivery**
- Membuat direktori baru pada direktori utama proyek untuk membuat berkas berupa template sadar untuk kerangka web
- Menambahkan direktori yang dibuat kedalam settings.py agar terdeteksi oleh aplikasi
- Membuat berkas baru untuk struktur forms yang berfungsi menerima object baru
- Tambahkan beberapa import kedalam views.py pada direktori aplikasi dan menambahkan beberapa fungsi agar dapat memproses penambahan objek dan pemrosesan data form. Selain itu tambahkan beberapa fungsi juga untuk melihat kerangka kode dalam bentuk JSON ataupun XML
- Ubah bagian tampilan utama agar dapat mengakomodasi perubahan yang terjadi pada kode dan menerima request
- Menambahkan urlpatterns baru pada urls.py agar dapat mengakomodasi perubahan yang dilakukan
- Tambahkan fungsi CRSF pada settings.py proyek

**Link screenshot postman:** https://drive.google.com/drive/folders/1uq8GAHIe9jSARbpZ5TNCCe8-r8HI-YB9?usp=sharing

## Tugas 4

**Django AuthenticationForm beserta kelebihan dan kekurangannya**

AuthenticationForm adalah Form bawaan di django.contrib.auth.forms untuk menangani proses login . Form ini menyediakan validasi yang akan memanggil `authenticate()`, pesan error standar, termasuk pengecekan akun inactive dan pola yang aman untuk login.

**Kelebihan**
- Siap pakai, khususnya dengan fitur validasi input, pesan error, integrasi langsung dengan `authenticate()` dan sistem auth Django.
- Mendukung penerimaan request di konstruktor yang akan sangat berguna bila backend butuh request.
- Mudah diganti/subclass jika perlu custom checks.

**Kekurangan**
- Defaultnya mengasumsikan ada field username; untuk custom user model yang menggunakan email sebagai identifier perlu perubahan/subclassing.
- Tidak menyediakan fitur "remember me" / pengaturan expiry session otomatis.
- Bukan solusi siap pakai untuk API.

**Perbedaan Autentikasi dan Otorisasi berserta penerapannya di Django**

**Autentikasi (Authentication):** memastikan identitas pengguna umunya melalui proses login yang melibatkan username/password.

**Otorisasi (Authorization): menentukan hal yang boleh dilakukan pengguna  seperti permissions, akses resource, dsb.**

**Implementasi oleh Django**

**Authentication:** fungsi `authenticate()` + `login()` yang berguna untuk memasukkan user ke session. request.user menjadi objek User atau dalam kasus anonim, maka AnonymousUser. Django menyediakan views/forms helpers dan backends untuk kustomisasi. 

**Authorization:** Django menyediakan model permission seperti add/change/delete, user.has_perm('app.codename'), @permission_required, dan Group untuk mengelompokkan permission. Selain itu ada decorator @login_required / mixin LoginRequiredMixin untuk membatasi view hanya untuk pengguna terautentikasi.

**Kelebihan dan kekurangan Session dan Cookies**

**Cookies**
- Mudah diproses, dimana browser menyimpan key/value, tersedia di request berikutnya.
- Kapasitas terbatas, mudah diubah oleh client, dan bisa terekspos ke XSS jika tidak HttpOnly.
- Perlu menambahkan mekanisme signing/encryption jika menyimpan data sensitif.

**Sessions**
- Data session disimpan server-side (DB/cache/file). Client hanya menerima session id.
- Kapasitas lebih besar & dapat menyimpan tipe data Python yang lebih kompleks.
- Butuh penyimpanan server-side (DB/cache).
- Jika menggunakan cookie-based sessions, data ditandatangani tetapi tidak terenkripsi yang artinya bisa dilihat oleh client walau tidak bisa dipalsukan tanpa SECRET_KEY.

**Resiko keamanan cookies dan penaggulangannya**

**Risiko utama**
- Adanya serangan XSS yang berupa script yang tidak diinginkan di halaman website, XSS dapat membaca cookie kecuali cookie diberi HttpOnly.
- Peretasan melalui teknik Man-in-the-middle (MITM), dimana cookie tanpa Secure dapat dikirim lewat HTTP yang tidak terenkripsi.
- Fitur CSRF yang mana cookies dikirim otomatis oleh browser sehingga rentan terhadap CSRF jika tidak ada proteksi.
- Rawan terhadap pengintaian client karena cookie ditaruh di client sehingga nilainya dapat dilihat kecuali terenkripsi.

**Praktik / mitigasi (Django + web)**

Django telah menyediakan berbagai fitur keamanan seperti:
- HttpOnly untuk cookie session dalam mencegah akses JS
- Secure yang hanya akan mengirim lewat HTTPS
- SameSite (Lax/Strict) untuk mengurangi CSRF via cross-site requests.
- CSRF middleware yang bertujuan untuk  mengaktifkan CSRF protection by default untuk POST forms.

**Step by step implementation:**
- Membuat template yang dibutuhkan seperti file template login dan register
- Mengimport semua library yang dibutuhkan untuk pengembangan
- Membuat form login, register untuk menampung input user
- Membuat fungsi login, register, logout untuk menjalankan proses yang bersangkutan
- Melakukan otorisasi dengan menambahkan dekorator @login_required pada fungsi yang menampilkan halaman utama dan produk
- Menambahkan fungsi cookies pada session pengguna
- Menambahkan path yang bersangkutan dari fungsi di views.py ke urls.py pada direktori aplikasi
- Hubungkan model untuk menanggapi perubahan model yang terjadi selama pengembangan
- Ubah tampilan utama website untuk mengakomodasi fungsi baru yang diterapkan

## Tugas 5

**Implementasi Fungsi Hapus dan Edit Product**

Pada pengembangan aplikasi web Django, implementasi fungsi hapus dan edit product dilakukan dengan membuat view functions khusus. Untuk edit product, dibuat fungsi `edit_product()` yang menerima parameter ID product, melakukan validasi kepemilikan product menggunakan `get_object_or_404()` dengan filter `user=request.user`, kemudian memproses form edit menggunakan `ProductForm`. Untuk hapus product, fungsi `delete_product()` dibuat dengan mekanisme serupa namun menggunakan method `DELETE` dan konfirmasi penghapusan. Kedua fungsi dilindungi dengan decorator `@login_required` untuk keamanan dan menggunakan Django messages framework untuk memberikan feedback kepada user.

**Urutan Prioritas CSS Selector**

Urutan prioritas CSS selector ditentukan oleh spesifisitas dengan urutan sebagai berikut:
1. **Inline styles** (style attribute dalam HTML)
2. **ID selectors** (#header) 
3. **Class selectors** (.button), attribute selectors ([type="text"]), dan pseudo-classes (:hover)
4. **Element selectors** (div, p) dan pseudo-elements (::before)

Ketika terjadi konflik, selector dengan prioritas lebih tinggi akan mengambil alih. Jika prioritas sama, CSS yang dideklarasikan terakhir dalam stylesheet yang akan diterapkan.

**Pentingnya Responsive Design**

Responsive design menjadi konsep krusial karena:
- **Multi-device usage**: Pengguna mengakses web dari berbagai perangkat dengan ukuran layar berbeda
- **User experience**: Memastikan pengalaman konsisten dan optimal di semua device
- **SEO benefits**: Google memprioritaskan situs yang mobile-friendly
- **Maintenance efficiency**: Satu codebase untuk semua device

**Contoh yang menerapkan**: Amazon, Netflix, Spotify - tampilan menyesuaikan sempurna dari desktop ke mobile
**Contoh belum menerapkan**: Website pemerintah lama, aplikasi web legacy

**Perbedaan Margin, Border, dan Padding**

Ketiga properti CSS ini mengatur spacing elemen dengan cara berbeda:
- **Padding**: Ruang antara konten elemen dan border-nya (dalam border)
- **Border**: Garis pembatas antara padding dan margin
- **Margin**: Ruang di luar border, memisahkan elemen dari elemen lain

**Implementasi**:
```css
.element {
    padding: 20px;    /* Ruang dalam */
    border: 2px solid #000; /* Garis batas */
    margin: 10px;     /* Ruang luar */
}
```

**Konsep Flexbox dan Grid Layout**

**Flexbox**:
- Layout satu dimensi (horizontal atau vertical)
- Ideal untuk komponen kecil seperti navigation bars, card layouts
- Mengatur item dalam container fleksibel dengan properti seperti `flex-direction`, `justify-content`, `align-items`

**Grid Layout**:
- Layout dua dimensi (baris dan kolom sekaligus)
- Cocok untuk layout halaman kompleks dan gallery
- Menggunakan `grid-template-columns`, `grid-template-rows` untuk mendefinisikan struktur

**Kegunaan**: Flexbox untuk alignment dan distribusi item dalam satu axis, Grid untuk layout kompleks dengan kontrol precise pada kedua dimensions.

**Step by step implementation**
- Tambahkan framework styling seperti Tailwind/CSS kedalam aplikasi
- Buat fitur edit news dan delete news pada views.py tambahkan fungsi pada urls.py dan tampilkan di web
- Tambahkan navigation bar dengan membuat berkas html untuk navigation bar di folder templates pada direktori utama
- Tambahkan navbar pada kode template main.html di folder template pada direktori aplikasi
- Buat static files dengan menambahkan middleware whitenoise
- Konfigurasi settings.py untuk mengatur STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL
- Tambahkan styling dan script tailwind ke berkas base.html pada folder template di direktori utama
- Tambahkan styling pada global.css sebagai styling default
- Lakukan styling pada setiap fitur yang diimplementasikan

## Tugas 6

**Perbedaan antara Synchronous dan Asynchronous Request**

**Synchronous request** adalah proses dimana browser mengirimkan request ke server dan harus menunggu hingga mendapatkan response sebelum dapat melanjutkan eksekusi kode lainnya. Dalam model ini, pengguna tidak dapat berinteraksi dengan halaman web selama proses request-response berlangsung, dan biasanya ditandai dengan loading indicator atau halaman yang freeze. Contohnya adalah ketika melakukan form submission tradisional dimana halaman akan sepenuhnya reload setelah data diproses.

**Asynchronous request** memungkinkan browser untuk mengirim request ke server tanpa harus menunggu response sebelum melanjutkan eksekusi kode lainnya. Pengguna tetap dapat berinteraksi dengan halaman web selama proses request berjalan di background. AJAX (Asynchronous JavaScript and XML) adalah implementasi umum dari asynchronous request, dimana hanya bagian tertentu dari halaman yang diperbarui tanpa perlu reload seluruh halaman.

**Alur Kerja AJAX di Django**

AJAX bekerja di Django melalui alur request-response yang terstruktur. Pertama, JavaScript di client-side mengirimkan HTTP request (biasanya menggunakan Fetch API atau XMLHttpRequest) ke endpoint Django yang telah ditentukan. Request ini dapat membawa data dalam format FormData, JSON, atau query parameters. Kemudian, Django menerima request di views yang sesuai, memproses data tersebut (validasi, penyimpanan ke database, dll), dan mengembalikan response dalam format JSON, XML, atau plain text. Di sisi client, JavaScript menerima response tersebut dan memperbarui tampilan halaman secara dinamis tanpa perlu reload, menggunakan DOM manipulation untuk menampilkan data baru atau feedback kepada pengguna.

**Keuntungan Menggunakan AJAX dibanding Render Biasa**

Penggunaan AJAX menawarkan beberapa keuntungan signifikan dibandingkan render tradisional di Django. Dari segi user experience, AJAX memberikan interaktivitas yang lebih baik dengan update konten yang seamless tanpa reload halaman, mengurangi waiting time yang dirasakan pengguna. Performa aplikasi juga meningkat karena hanya data yang diperlukan yang ditransfer, bukan seluruh halaman HTML, sehingga menghemat bandwidth dan waktu loading. Selain itu, AJAX memungkinkan pembuatan single-page application (SPA) yang lebih modern dan responsif, serta memberikan feedback yang lebih immediate kepada pengguna melalui update partial content dan real-time validation.

**Keamanan AJAX untuk Fitur Login dan Register**

Memastikan keamanan saat menggunakan AJAX untuk fitur autentikasi memerlukan beberapa pertimbangan penting. CSRF (Cross-Site Request Forgery) protection harus diimplementasikan dengan menyertakan CSRF token dalam setiap AJAX request, baik melalui header X-CSRFToken atau sebagai data dalam request. Validasi data harus dilakukan secara ketat di server-side meskipun sudah dilakukan di client-side, karena client-side validation dapat dengan mudah di-bypass. Penggunaan HTTPS wajib diterapkan untuk mengenkripsi data sensitif seperti kredensial login selama transmisi. Rate limiting perlu diimplementasikan untuk mencegah brute force attacks, dan session management yang aman harus dijaga dengan pengaturan cookie yang tepat (HttpOnly, Secure flags).

**Pengaruh AJAX terhadap User Experience**

AJAX secara signifikan meningkatkan pengalaman pengguna pada website melalui berbagai aspek. Responsivitas aplikasi meningkat drastis karena aksi pengguna dapat langsung mendapatkan feedback tanpa menunggu reload halaman, menciptakan feeling yang lebih natural dan aplikatif. Interaksi yang lebih dinamis memungkinkan update konten secara real-time, validasi form yang immediate, dan animasi transisi yang smooth. Pengguna dapat melanjutkan pekerjaan mereka tanpa interupsi yang disebabkan oleh page refresh, sehingga flow kerja menjadi tidak terputus. Secara keseluruhan, AJAX menciptakan pengalaman web yang lebih modern, cepat, dan engaging, mendekati pengalaman menggunakan aplikasi desktop native.