# Laporan Proyek Machine Learning - Ni Made Yuli Cahyani

## Project Overview

<p align="center">
    <img src=https://user-images.githubusercontent.com/71582007/141651018-0a3c2e7a-e9b6-4402-be87-11dda8b103df.jpg>
</p>

Buku adalah jendela dunia. Dengan buku seseorang dapat menjelajah ke dunia luar tanpa perlu pergi ke dunia luar. Dengan buku seseorang dapat memperoleh pengetahuan yang tiada batas, melintas waktu, dan mengenal seseorang dari seluruh belahan dunia, karena buku merupakan sumber ilmu pengetahuan. Untuk dapat memperoleh ilmu yang ada di dalam buku, seseorang harus membaca buku [[1](https://media.neliti.com/media/publications/96720-ID-rumah-baca-jendela-dunia-sebuah-model-pe.pdf)]. Kegiatan membaca buku sangat penting bagi kehidupan manusia, dengan terbiasa membaca buku maka seseorang akan memiliki cakrawala pengetahuan yang luas [[2](https://journal.iainkudus.ac.id/index.php/Libraria/article/download/1189/1082)]. Namun dengan banyaknya jumlah buku yang tersedia terkadang membuat pembaca kebingungan dalam menentukan buku yang hendak mereka baca. Terkadang dijumpai pembaca yang hanya ingin membaca buku-buku yang dengan reputasi penjualan terbaik. Ada pula pembaca yang hanya ingin membaca buku yang mirip dengan buku-buku yang pernah dibaca sebelumnya. Tidak jarang juga ditemui pembaca yang menentukan buku-buku yang akan dibaca selanjutnya berdasarkan rating dari buku-buku yang telah dilihatnya. Semakin tinggi rating dari buku tersebut, semakin tertarik pula pembaca untuk membacanya. Semakin rendah rating dari buku tersebut, maka pembaca cenderung enggan untuk membacanya [[3](http://eprints.undip.ac.id/65823/1/laporan_24010311130044_1.pdf)].

Berdasarkan permasalahan tersebut, pada proyek ini akan dibuat suatu model sistem rekomendasi menggunakan teknik _collaborative filtering_  untuk merekomendasikan buku-buku yang mungkin akan dibaca oleh pengguna. _Collaborative filtering_ merupakan metode yang digunakan untuk merekomendasikan item berdasarkan penilaian pengguna sebelumnya, dimana attribut yang digunakan bukan konten tetapi _user behaviour_. Contohnya yaitu merekomendasikan suatu item berdasarkan dari riwayat rating dari user tersebut maupun user lain [[4](https://medium.com/@ranggaantok/bagaimana-sistem-rekomendasi-berkerja-e749dac64816)]. Dengan adanya sistem rekomendasi ini diharapkan dapat membantu pengguna mendapatkan rekomendasi buku-buku yang sesuai dengan preferensi pengguna di masa lalu, buku-buku yang mungkin disukai dan belum pernah dibaca oleh pengguna.

## Business Understanding

### Problem Statements

Berdasarkan penjelasan pada project overview, berikut ini merupakan rincian masalah yang perlu diselesaikan di proyek ini:

-   Sistem rekomendasi apa yang baik untuk diterapkan pada kasus ini?
-   Bagaimana cara membuat sistem rekomendasi buku yang mungkin disukai dan belum pernah dibaca oleh pengguna?

### Goals

Tujuan dibuatnya proyek ini adalah sebagai berikut :
-   Membuat sistem rekomendasi buku sesuai dengan preferensi pengguna.
-   Memberikan rekomendasi buku yang mungkin disukai dan belum pernah dibaca oleh pengguna.

### Solution Approach

Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :

-   **Pra-pemrosesan Data**. Pada pra-pemrosesan data dapat dilakukan beberapa tahapan, antara lain :

    -   Menghapus kolom/fitur yang tidak diperlukan.
    -   Mengganti tipe data pada kolom.
    -   Membersihkan data kosong pada kolom.
    -   Melakukan _text cleaning_ pada data.

-   **Persiapan Data**. Pada persiapan data dapat dilakukan beberapa tahapan, antara lain :

    -   Persiapan data untuk model KNN.
        -   Filtering data buku dengan jumlah rating >= threshold (30)
        -   Membuat pivot tabel.
    -   Persiapan data untuk model Deep Learning.
        -   Melakukan proses encoding fitur user_id dan isbn ke dalam indeks integer.
        -   Pembagian Data untuk Training dan Validasi

-   **Pembangunan Model**. Pada proyek ini sistem rekomendasi yang dibuat menggunakan teknik _collaborative filtering_ karena sesuai dengan dataset yang akan digunakan. Sehingga sistem rekomendasi dibuat untuk memberikan rekomendasi pada pengguna terhadap buku yang mirip dengan preferensi pengguna di masa lalu. Pada pembangunan model sistem rekomendasi terdapat beberapa pendekatan yang digunakan, antara lain :
    -   **Dengan pendekatan Item-Based dengan algoritma K-Nearest Neighbor.**
        <br> Item-based collaborative filtering merupakan metode rekomendasi yang bekerja berdasarkan adanya kesamaan antara  pemberi rating terhadap item yang dituju. Dari tingkat kesamaan item, kemudian dibagi berdasarkan parameter kebutuhan pelanggan untuk memperoleh nilai kegunaan item. Item yang memiliki nilai tertinggi maka akan dijadikan rekomendasi [[5](https://ejournal.upi.edu/index.php/JATIKOM/article/download/33208/14281)]. Kemudian algoritma yang digunakan pada pendekatan ini yaitu  K-Nearest Neighbor (KNN) karena mudah digunakan dan dapat mengantisipasi jika pengguna kurang paham  dengan apa yang ingin dicari karena metode ini menerapkan prinsip pencarian menggunakan jarak kedekatan (kemiripan data) sampel  dengan  data  yang  ada [[6](https://journals.telkomuniversity.ac.id/tektrika/article/view/1846/1141)]. Kelebihan dan kekurangan algoritma K-Nearest Neighbor adalah sebagai berikut (bersumber dari [[6](https://journals.telkomuniversity.ac.id/tektrika/article/view/1846/1141)]) :
    
        -   Kelebihan :
            -   Keakuratan hasil yang diperoleh lebih dijamin
            -   Untuk Data Training yang besar, hasilnya akan lebih efektif.
        -   Kekurangan :
            -   Berdasarkan perhitungan nilai jarak (Distance Based Learning), tidak jelas atribut mana yang memberikan hasil yang baik dan perhitungan jarak mana yang sebaiknya digunakan,
            -   Peneliti perlu menghitung nilai baru ke semua data yang ada pada Data Training dan menghitung jarak karena nilai komputasinya tinggi
            -   Parameter K perlu ditunjukkan (jumlah tetangga terdekat).
            
    -   **Dengan pendekatan Deep learning atau Neural Network.**
        <br>Deep learning merupakan subbidang machine learning yang algoritmanya terinspirasi dari struktur otak manusia. Struktur tersebut dinamakan Artificial Neural Networks atau disingkat ANN. Pada dasarnya, ia merupakan jaringan saraf yang memiliki tiga atau lebih lapisan ANN. Ia mampu belajar dan beradaptasi terhadap sejumlah besar data serta menyelesaikan berbagai permasalahan yang sulit diselesaikan dengan algoritma machine learning lainnya 
[[7](https://www.dicoding.com/blog/mengenal-deep-learning/)]. Penerapan metode Deep Learning menjadi salah satu metode yang populer untuk sistem rekomendasi. Penggunaan metode Deep Learning pada sistem rekomendasi lebih efisien dan tepat sasaran. Beberapa kelebihan penerapan Deep Learning adalah sebagai berikut (bersumber dari [[6](https://journals.telkomuniversity.ac.id/tektrika/article/view/1846/1141)]) :
        
        -   Dapat memproses unstructured data seperti teks dan gambar.
        -   Dapat mengotomatisasi proses ekstraksi fitur tanpa perlu melakukan proses pelabelan secara manual.
        -   Memberikan hasil akhir yang berkualitas.
        -   Dapat mengurangi biaya operasional.
        -   Dapat melakukan manipulasi data dengan lebih efektif.

## Data Understanding

### Informasi Dataset

Dataset yang digunakan pada proyek ini yaitu Book-Crossing dataset, informasi lebih lanjut  mengenai dataset tersebut dapat lihat pada tabel berikut:

<img width="719" alt="informasi-dataset" src="https://user-images.githubusercontent.com/71582007/141651042-5d94ef43-5aba-4568-8ca2-cb34496040ce.PNG">

| Jenis                   | Keterangan                                                                              |
| ----------------------- | --------------------------------------------------------------------------------------- |
| Sumber                  | [Kaggle Dataset : Book-Crossing](https://www.kaggle.com/ruchi798/bookcrossing-dataset)  |
| Dataset Owner           | Ruchi Bhatia                                                                            |
| Lisensi                 | CC0: Public Domain                                                                      |
| Kategori                | Arts and Entertainment, Online Communities, Literature                                  |
| Rating Penggunaan       | 10.0 (Gold)                                                                             |
| Jenis dan Ukuran Berkas | zip (600.34 MB)                                                                         |

Setelah melakukan observasi pada dataset yang diunduh pada kaggle, didapatakan informasi sebagai berikut :
  
-   Terdapat 1031175 baris (records atau jumlah pengamatan) dalam Book-Crossing dataset.
-   Terdapat 19 kolom yaitu 'Unnamed: 0', 'user_id', 'location', 'age', 'isbn', 'rating', 'book_title', 'book_author', 'year_of_publication', 'publisher', 'img_s', 'img_m', 'img_l', 'Summary', 'Language', 'Category', 'city', 'state', 'country'.
-   Terdapat 3 kolom numerik dengan tipe data int64, yaitu: Unnamed: 0, user_id, rating. Ini merupakan fitur numerik. Tetapi untuk kolom Unnamed: 0 merupakan fitur yang tidak diperlukan dan bisa dibuang. 
-   Terdapat 2 kolom numerik dengan tipe data float64 yaitu: age dan year_of_publication. Ini merupakan fitur numerik.
-   Terdapat 14 kolom dengan tipe object, yaitu: location, isbn, book_title, book_author, publisher, img_s, img_m, img_l, Summary, Language, Category, city, state, country. Kolom ini merupakan categorical features (fitur non-numerik) dimana kolom ini merupakan target fitur.
-   Tidak terdapat data duplikat pada dataset. 
  
 Untuk penjelasan mengenai variabel-variable pada Book-Crossing dataset dapat dilihat pada poin-poin berikut ini:

  - `Unnamed: 0` - index pada data
  - `user_id` - id dari pengguna
  - `location` - lokasi/alamat pengguna
  - `age` - umur pengguna
  - `isbn` - kode ISBN (International Standard Book Number) buku
  - `rating` - rating dari buku
  - `book_title` - judul buku
  - `book_author` - penulis buku
  - `year_of_publication` - tahun terbit buku
  - `publisher` - penerbit buku
  - `img_s` - gambar sampul buku (small)
  - `img_m` - gambar sampul buku (medium)
  - `img_l` - gambar sampul buku (large)
  - `Summary` - ringkasan/sinopsis buku
  - `Language` - bahasa yang digunakan buku
  - `Category` - kategori buku
  - `city` - kota pengguna
  - `state` - negara bagian penguna
  - `country` - negara pengguna

### Data Preprocessing

-   Menghapus kolom/fitur yang tidak diperlukan.
-   Mengganti tipe data pada kolom.
-   Membersihkan data kosong pada kolom.
-   Melakukan _text cleaning_ pada data.

### Data Visualization

-   Top 10 dari tahun penerbitan, penulis dan buku.
-   Distribusi rating buku dan umur user.
-   Wordcloud pada judu, penulis dan penerbit buku.

## Data Preparation
-   Persiapan data untuk model KNN.
    -   Filtering data buku dengan jumlah rating >= threshold (30)
    -   Membuat pivot tabel.
-   Persiapan data untuk model Deep Learning.
    -   Melakukan proses encoding fitur user_id dan isbn ke dalam indeks integer.
    -   Pembagian Data untuk Training dan Validasi
## Modeling

-   Dengan pendekatan Item-Based dengan algoritma K-Nearest Neighbor.
-   Dengan pendekatan Deep learning atau Neural Network.

## Evaluation

## _Referensi:_

[[1](https://media.neliti.com/media/publications/96720-ID-rumah-baca-jendela-dunia-sebuah-model-pe.pdf)] Gresi A.R., Alan N., Khasanah B.R., Robby A.S., Priyadi N.P. (2013). _Rumah Baca Jendela Dunia, Sebuah Model Perpustakaan Panti Asuhan_. Jurnal Ilmiah Mahasiswa, Vol. 3 No.2. https://media.neliti.com/media/publications/96720-ID-rumah-baca-jendela-dunia-sebuah-model-pe.pdf

[[2](https://journal.iainkudus.ac.id/index.php/Libraria/article/download/1189/1082)] Shofaussamawati. (2014). _Menumbuhkan Minat Baca dengan Pengenalan Perpustakaan Pada Anak Sejak Dini_. Jurnal IAIN, Vol. 2 No.1. https://journal.iainkudus.ac.id/index.php/Libraria/article/download/1189/1082

[[3](http://eprints.undip.ac.id/65823/1/laporan_24010311130044_1.pdf)] Ritdrix, A.H. (2018). _Sistem Rekomendasi Buku Menggunakan Metode Item-Based Collaborative Filtering_. Universitas Diponegoro. http://eprints.undip.ac.id/65823/1/laporan_24010311130044_1.pdf

[[4](https://medium.com/@ranggaantok/bagaimana-sistem-rekomendasi-berkerja-e749dac64816)] Rangga, R. A. (2018). _Bagaimana Sistem Rekomendasi Berkerja?_. Medium. https://medium.com/@ranggaantok/bagaimana-sistem-rekomendasi-berkerja-e749dac64816

[[5](https://ejournal.upi.edu/index.php/JATIKOM/article/download/33208/14281)] Agustian, E. R., Munir, Nugroho, E. P. (2020). _Sistem Rekomendasi Film Menggunakan Metode Collaborative Filtering dan K-Nearest Neighbors_.Jurnal Aplikasi dan Teori Ilmu Komputer, Vol. 3 No. 1. https://ejournal.upi.edu/index.php/JATIKOM/article/download/33208/14281

[[6](https://journals.telkomuniversity.ac.id/tektrika/article/view/1846/1141)] Gusti, I. G., Nasrun, M., Nugrahaeni, R. A. (2020). _Rekomendasi Sistem Pemilihan Mobil Menggunakan K-Nearest Neighbor (KNN) CollaborativeE Filtering_.Jurnal TEKTRIKA, Vol.4, No.1. https://journals.telkomuniversity.ac.id/tektrika/article/view/1846/1141

[[7](https://www.dicoding.com/blog/mengenal-deep-learning/)] Setiawan, R. (2021). _Mengenal Deep Learning Lebih Jelas_.Dicoding. https://www.dicoding.com/blog/mengenal-deep-learning/
