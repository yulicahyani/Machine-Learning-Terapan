# Laporan Proyek Machine Learning - Ni Made Yuli Cahyani
## Domain Proyek

Domain proyek yang dipilih dalam proyek _machine learning_ ini adalah mengenai **pertanian** dengan judul proyek "Prediksi Tanaman yang Cocok untuk Ditanam di Lahan Pertanian Tertentu".

-   Latar Belakang

Sektor pertanian di Indonesia hingga saat ini memegang peranan penting dalam perekonomian nasional dan pembangunan negara secara keseluruhan. Pertanian masih menjadi andalan sebagai sumber bahan pangan [[1](https://setkab.go.id/posisi-pertanian-yang-tetap-strategis-masa-kini-dan-masadepan/)] dan sumber mata pencaharian terbesar di Indonesia bahkan hampir di setiap daerah di Indonesia terdapat lahan pertanian [[2](https://prosiding.senadi.upy.ac.id/index.php/senadi/article/view/164)]. Sebelum melakukan proses pertanian maka seorang petani harus mengumpulkan berbagai informasi yang dapat mempengaruhi proses pertanian terlebih dahulu. Informasi yang diperlukan antara lain seperti karaktersistik, struktur dan tekstur lahan, jenis tanaman yang akan ditanam, dan target panen [[3](https://medium.com/@auliagusningati/precision-agriculture-precision-farming-dan-digital-farming-fe77ba131be6)]. Namun pada kenyataannya, dalam melakukan penanaman tanaman pada suatu lahan pertanian, tidak banyak petani yang memperhitungkan apakah lahan yang dimiliki cocok untuk ditanami jenis tanaman yang telah ditentukan atau tidak [[2](https://prosiding.senadi.upy.ac.id/index.php/senadi/article/view/164)]. Keputusan seorang petani mengenai jenis tanaman apa yang akan ditanam di lahannya pada umumnya tergantung pada intuisi petani itu sendiri, petani akan lebih memilih tanaman yang sedang tren di wilayah sekitarnya dan biasanya mereka tidak memiliki pengetahuan yang cukup tentang kandungan nutrisi lahan seperti nitrogen, fosfor, kalium dalam lahan [[6](https://www.ijert.org/crop-prediction-using-machine-learning-approaches)]. Sehingga, jika petani mengambil keputusan yang salah pada pemilihan tanaman maka hasil panen menjadi tidak optimal dan berpotensi mengalami kerugian yang cukup besar nantinya [[2](https://prosiding.senadi.upy.ac.id/index.php/senadi/article/view/164)].

Berdasarkan permasalahan di atas, maka pada proyek ini akan dibangun suatu model _machine larning_ untuk memprediksi jenis tanaman yang cocok ditanam di lahan pertanian tertentu berdasarkan parameter kandungan N, P, K (Nitrogen, Fosfor, Kalium) pada lahan, curah hujan, huhu, kelembaban dan pH. Dengan adanya model _machine learning_ ini, diharapkan dapat membantu dan memudahkan petani dalam mengambil keputusan tentang strategi pertanian khususnya dalam memilih jenis tanaman yang cocok untuk lahan mereka, sehingga dapat meminimalisir kesalahan penanaman serta dapat meningkatkan hasil produksi di sektor pertanian. Kemudian untuk tahap pengembangan selanjutnya implementasi dari model ini dapat dijalankan pada sebuah aplikasi berbasis web ataupun android.


## Business Understanding

### Problem Statements
Berdasarkan pada latar belakang di atas, permasalahan yang dapat diselesaikan pada proyek ini adalah sebagai berikut :

-   Bagaimana cara melakukan pra-pemrosesan data lahan sehingga dapat digunakan untuk membuat model yang baik?
-   Bagaimana cara membangun model _machine learning_ untuk mengklasifikasikan data lahan ke dalam jenis tanaman yang cocok ditanam pada lahan tersebut?

### Goals
Tujuan dibuatnya proyek ini adalah sebagai berikut :

-   Melakukan pra-pemrosesan data lahan agar dapat digunakan dalam membangun model.
-   Membangun model _machine learning_ untuk mengklasifikasikan data lahan ke dalam jenis tanaman yang cocok ditanam pada lahan tersebut dengan tingkat akurasi > 75%.

### Solution statements
Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :

- **Pra-pemrosesan Data**. Pada pra-pemrosesan data dapat dilakukan beberapa tahapan, antara lain :
  
    -   Memeriksa _missing value_ pada data dan mengisinya dengan nilai rata rata atau _mean substitution_ jika ditemukan _missing value_ pada data.
    -   Melakukan pembagian dataset menjadi dua bagian dengan rasio 80% untuk data latih dan 20% untuk data uji.
    -   Menghapus data pencilan (_outlier_) pada data latih dengan metode LOF (_Local Outlier Factor_).
    -   Melakukan standardisasi data pada semua fitur numerik pada dataset.
  
- **Pembangunan Model**. Pada pembangunan model terdapat beberapa algorima yang digunakan, antara lain :

  - **K-Nearest Neighbor**. 
    <br>K-Nearest Neighbor atau KNN adalah algoritma yang relatif sederhana dibandingkan dengan algoritma lain. Algoritma KNN menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan. KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k-tetangga terdekat. KNN bisa digunakan untuk kasus klasifikasi dan regresi [[7](https://towardsdatascience.com/getting-acquainted-with-k-nearest-neighbors-ba0a9ecf354f)]. Cara kerja algoritma KNN adalah sebagai berikut (bersumber dari [[4](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]) :
    
    -   Inisialisasi nilai K (jumlah tetangga)
    -   Hitung jarak antara data baru yang ditanyakan dengan seluruh sampel data pelatihan
    -   Urutkan seluruh jarak berdasarkan jarak minimum dan tetapkan jumlah tetangga (nearest neighbors) sesuai dengan nilai K
    -   Pilih sejumlah K data dengan jarak terdekat
    -   Kemudian tentukan kelas atau label dari data baru
    
    Kelebihan dan kekurangan algoritma K-Nearest Neighbor adalah sebagai berikut (bersumber dari [[4](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]) :
    
    -   Kelebihan :
        -   Algoritma KNN merupakan algoritma yang sederhana dan mudah untuk diimplementasikan
        -   Algoritma KNN dapat diimplementasikan pada beberapa kasus seperti klasifikasi, regresi dan pencarian
    -   Kekurangan :
        -   Algoritma KNN menjadi lebih lambat secara signifikan seiring meningkatnya jumlah sampel dan/atau variabel independen

  - **Random Forest**. Kalimat selanjutnya menjelaskan informasi atau cara kerja algoritma ini. Selain itu, dapat juga Anda tambahkan kelebihan dan kekurangan algoritma ini.
  - **XGBoost Algorithm**. Sama dengan di atas. 

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

## Data Preparation
Pada bagian ini Anda menjelaskan teknik yang digunakan pada tahapan Data Preparation. 
- Terapkan minimal satu teknik data preparation dan jelaskan proses yang dilakukan.
- Jelaskan alasan mengapa Anda perlu menerapkan teknik tersebut pada tahap Data Preparation. 

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. 

Jelaskan bagaimana Anda melakukan proses modeling dalam proyek. Misalnya, Anda menggunakan satu algoritma kemudian melakukan improvement dari baseline model atau Anda menggunakan dua atau lebih algoritma kemudian membandingkan performanya.

Sajikan model terbaik Anda sebagai solusi.
Jelaskan pula hasil dari model Anda (misal, hasil prediksi).

## Evaluation
Bagian ini menjelaskan mengenai metrik evaluasi yang digunakan untuk mengukur kinerja model. Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan dan bagaimana formulanya
- Kelebihan dan kekurangan metrik
- Bagaimana cara menerapkannya ke dalam kode.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

## _Referensi:_

[[1](https://setkab.go.id/posisi-pertanian-yang-tetap-strategis-masa-kini-dan-masadepan/)] Setiawan, A. 2014. _Posisi Pertanian Yang Tetap Strategis Masa Kini dan Masa Depan_. https://setkab.go.id/posisi-pertanian-yang-tetap-strategis-masa-kini-dan-masadepan/

[[2](https://prosiding.senadi.upy.ac.id/index.php/senadi/article/view/164)] Nugroho, F. A., Oyama, S., Riyadi, A. (2020). _Sistem Pendukung Keputusan Menentukan Jenis Tanaman Pada Lahan Pertanian Berdasarkan Letak Geografis dan Curah Hujan Menggunakan Metode Rule Based System_. Prosiding dalam Seminar Nasional Dinamika Informatika, Vol 4, No 1. https://prosiding.senadi.upy.ac.id/index.php/senadi/article/view/164

[[3](https://medium.com/@auliagusningati/precision-agriculture-precision-farming-dan-digital-farming-fe77ba131be6)] Gusning, A. (20120, Aug 1). _Precision Agriculture, Precision Farming dan Digital Farming_. Medium. https://medium.com/@auliagusningati/precision-agriculture-precision-farming-dan-digital-farming-fe77ba131be6

[[4](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)] Harrison, O. (2019, July 14). _Machine Learning Basics with the K-Nearest Neighbors Algorithm_. Medium. https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

[[5](https://statisticsbyjim.com/basics/remove-outliers/)] Frost, J. (2021, April 5). _Guidelines for Removing and Handling Outliers in Data._ Statistics By Jim. https://statisticsbyjim.com/basics/remove-outliers/

[[6](https://www.ijert.org/crop-prediction-using-machine-learning-approaches)] Mahendra, N., Vishwakarma, D., Nischitha, K., Ashwini, Manjuraju, M. R. (2020). _Crop Prediction using Machine Learning Approaches_. International Journal of Engineering Research & Technology, Vol 09, Issue 08. https://www.ijert.org/crop-prediction-using-machine-learning-approaches

[[7](https://towardsdatascience.com/getting-acquainted-with-k-nearest-neighbors-ba0a9ecf354f)] Raj, A. (2021, Apr 8). _Introduction to Classification Using K Nearest Neighbours_. Medium. https://towardsdatascience.com/getting-acquainted-with-k-nearest-neighbors-ba0a9ecf354f
