# Laporan Proyek Machine Learning - Ni Made Yuli Cahyani

## Project Overview
Buku adalah jendela dunia. Dengan buku seseorang dapat menjelajah ke dunia luar tanpa perlu pergi ke dunia luar. Dengan buku seseorang dapat memperoleh pengetahuan yang tiada batas, melintas waktu, dan mengenal seseorang dari seluruh belahan dunia, karena buku merupakan sumber ilmu pengetahuan. Untuk dapat memperoleh ilmu yang ada di dalam buku, seseorang harus membaca buku [[1](https://media.neliti.com/media/publications/96720-ID-rumah-baca-jendela-dunia-sebuah-model-pe.pdf)]. Kegiatan membaca buku sangat penting bagi kehidupan manusia, dengan terbiasa membaca buku maka seseorang akan memiliki cakrawala pengetahuan yang luas [[2](https://journal.iainkudus.ac.id/index.php/Libraria/article/download/1189/1082)]. Namun dengan banyaknya jumlah buku yang tersedia terkadang membuat pembaca kebingungan dalam menentukan buku yang hendak mereka baca. Terkadang dijumpai pembaca yang hanya ingin membaca buku-buku yang dengan reputasi penjualan terbaik. Ada pula pembaca yang hanya ingin membaca buku yang mirip dengan buku-buku yang pernah dibaca sebelumnya. Tidak jarang juga ditemui pembaca yang menentukan buku-buku yang akan dibaca selanjutnya berdasarkan rating dari buku-buku yang telah dilihatnya. Semakin tinggi rating dari buku tersebut, semakin tertarik pula pembaca untuk membacanya. Semakin rendah rating dari buku tersebut, maka pembaca cenderung enggan untuk membacanya [[3](http://eprints.undip.ac.id/65823/1/laporan_24010311130044_1.pdf)].

Berdasarkan permasalahan tersebut, pada proyek ini akan dibuat suatu model sistem rekomendasi menggunakan teknik _collaborative filtering_  untuk merekomendasikan buku-buku yang mungkin akan dibaca oleh pengguna. _Collaborative filtering_ merupakan metode yang digunakan untuk merekomendasikan item berdasarkan penilaian pengguna sebelumnya, dimana attribut yang digunakan bukan konten tetapi _user behaviour_. Contohnya yaitu merekomendasikan suatu item berdasarkan dari riwayat rating dari user tersebut maupun user lain. Dengan adanya sistem rekomendasi ini diharapkan dapat membantu pengguna mendapatkan rekomendasi buku-buku yang sesuai dengan preferensi pengguna di masa lalu, buku-buku yang mungkin disukai dan belum pernah dibaca oleh pengguna.

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
        -   Menghilangkan data buku dengan jumlah rating dibawah threshold (30).
        -   Membuat pivot tabel.
    -   Persiapan data untuk model Deep Learning.
        -   Melakukan proses encoding fitur user_id dan isbn ke dalam indeks integer.
        -   Pembagian Data untuk Training dan Validasi

-   **Pembangunan Model**. Pada proyek ini sistem rekomendasi yang dibuat menggunakan teknik _collaborative filtering_ karena sesuai dengan dataset yang akan digunakan. Sehingga sistem rekomendasi dibuat untuk memberikan rekomendasi pada pengguna terhadap buku yang mirip dengan preferensi pengguna di masa lalu. Pada pembangunan model sistem rekomendasi terdapat beberapa pendekatan yang digunakan, antara lain :
    -   Dengan pendekatan Item-Based dengan algoritma K-Nearest Neighbor.
        <br> Algoritma tersebut dipilih karena mudah digunakan dan juga cocok untuk kasus clustering di sistem rekomendasi.
    -   Dengan pendekatan Deep learning atau Neural Network.

## Data Understanding

### Informasi Dataset

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
    -   Menghilangkan data buku dengan jumlah rating dibawah threshold (30).
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

