# Laporan Proyek Machine Learning - Ni Made Yuli Cahyani

## Project Overview

Pada bagian ini, Kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.


## Business Understanding

### Problem Statements

Berdasarkan penjelasan pada project overview, berikut ini merupakan rincian masalah yang perlu diselesaikan di proyek ini:

-   Sistem rekomendasi apa yang baik untuk diterapkan pada kasus ini?
-   Bagaimana cara membuat sistem rekomendasi buku yang mungkin disukai dan belum pernah dibaca oleh pengguna?

### Goals

Tujuan dibuatnya proyek ini adalah sebagai berikut :
-   Membuat sistem rekomendasi buku sesuai dengan preferensi pengguna.
-   Memberikan rekomendasi buku yang mungkin disukai dan belum pernah dibaca oleh pengguna.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution Approach

Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :

-   Untuk bagian pra-pemrosesan data dilakukan beberapa teknik diantaranya :

    -   Memperbaiki tipe data pada setiap kolom.
    -   Mengimputasi data kosong pada kolom rating.
    -   Membersihkan data kosong pada kolom.
    -   Membersihkan data duplikasi.

    Setelah hal tersebut dilakukan, selanjutnya dilakukan visualisasi data yang dapat dilihat lebih lengkap pada bagian _Data Understanding_.

-   Untuk bagian persiapan data (sebelum dimasukkan ke model) dilakukan beberapa teknik diantaranya :

    -   Konversi label kategori menjadi _one-hot encoding_.
    -   Standarisasi label numerik.

-   Kemudian untuk sistem rekomendasi yang dibuat, dipilih sistem rekomendasi dengan teknik _collaborative filtering_ karena sesuai dengan dataset yang akan digunakan. Sehingga sistem rekomendasi dibuat untuk memberikan rekomendasi pada pengguna terhadap buku yang mirip dengan preferensi pengguna di masa lalu. Beberapa algoritma yang digunakan untuk membuat sistem rekomendasi di proyek ini diantaranya :

    -   Dengan pendekatan Deep learning atau Neural Network
    -   Dengan KNN Item-Based, yakni algoritma K-Nearest Neighbor. Algoritma tersebut dipilih karena mudah digunakan dan juga cocok untuk kasus clustering di sistem rekomendasi. Algoritma ini mengasumsikan bahwa sesuatu yang serupa pasti selalu berdekatan. Cara kerja algoritma ini adalah sebagai berikut (diterjemahkan dari [[3](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]):

        -   Muat datanya
        -   Inisialisasi nilai K (banyak tetangga/kelompok)
        -   Pada setiap datanya :
            -   Hitung euclidian distance antara contoh kueri dan contoh yang ada pada data tersebut dengan rumus seperti berikut ini :
                ![Rumus Euclidian Distance](https://user-images.githubusercontent.com/58651943/133823136-ede96318-8fa8-4e93-a35f-64a66e5b5fd0.png)
            -   Tambahkan jarak dan urutan dari contoh pada koleksi yang berururutan
        -   Pilih entri K paling awal pada koleksi yang berurutan
        -   Dapatkan label dari dari entri K yang dipilih
        -   Apabila kasus regresi, kembalikan nilai rata-ratanya. Apabila kasus klasifikasi, kembalikan labelnya.

        Selain itu, berikut ini merupakan kelebihan dan kekurangan algoritma dari K-Nearest Neighbor (diterjemahkan dari [[3](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]):

        -   Kelebihan :
            -   Algoritmanya mudah digunakan dan sederhana
            -   Algoritmanya sangat fleksibel, dapat diimplementasikan pada kasus klasifikasi, regresi dan pencarian
        -   Kekurangan :
            -   Algoritme menjadi lebih lambat secara signifikan karena jumlah contoh dan/atau prediktor/variabel yang meningkat.


## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.
