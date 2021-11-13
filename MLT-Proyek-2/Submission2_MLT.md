# Laporan Proyek Machine Learning - Ni Made Yuli Cahyani

## Project Overview

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
        -   Menyiapakan data buku dengan jumlah rating 30 atau lebih.
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
    -   Menyiapakan data buku dengan jumlah rating 30 atau lebih.
    -   Membuat pivot tabel.
-   Persiapan data untuk model Deep Learning.
    -   Melakukan proses encoding fitur user_id dan isbn ke dalam indeks integer.
    -   Pembagian Data untuk Training dan Validasi
## Modeling

-   Dengan pendekatan Item-Based dengan algoritma K-Nearest Neighbor.
-   Dengan pendekatan Deep learning atau Neural Network.

## Evaluation

## _Referensi:_

[[1](https://setkab.go.id/posisi-pertanian-yang-tetap-strategis-masa-kini-dan-masadepan/)] Setiawan, A. 2014. _Posisi Pertanian Yang Tetap Strategis Masa Kini dan Masa Depan_. https://setkab.go.id/posisi-pertanian-yang-tetap-strategis-masa-kini-dan-masadepan/
