# -*- coding: utf-8 -*-
"""Submission1_MLT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_TD7seYQPdvPSA7YoMH91IotYiwnRvIV

# **Analisis Prediktif**: Prediksi Jenis Tanaman yang Cocok untuk Ditanam di Lahan Pertanian Tertentu
---
##### Proyek Submission 1 - Machine Learning Terapan
##### Oleh : Ni Made Yuli Cahyani
![precisionag2909-620x330](https://user-images.githubusercontent.com/71582007/139696754-c9faa3ef-58e3-40a0-80fe-dd50d36c2f05.jpg)

# **Pendahuluan**

Pada proyek ini, topik yang dibahas adalah mengenai `pertanian` dimana pada proyek ini akan membangun model machine larning untuk memprediksi jenis tanaman yang cocok ditanam di lahan pertanian tertentu berdasarkan parameter kandungan N, P, K (Nitrogen, Fosfor, Kalium) pada lahan, curah hujan, huhu, kelembaban dan pH. Dengan adanya model machine learning ini, diharapkan dapat membantu dan memudahkan petani dalam mengambil keputusan tentang strategi pertanian khususnya dalam memilih jenis tanaman yang cocok untuk lahan mereka, sehingga dapat meminimalisir kesalahan penanaman serta dapat meningkatkan hasil produksi di sektor pertanian.

# **1. Mengimpor library python yang dibutuhkan**
"""

# Commented out IPython magic to ensure Python compatibility.
from google_drive_downloader import GoogleDriveDownloader as gdd

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import train_test_split

from sklearn.neighbors import  KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn import metrics
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, classification_report

"""# **2. Mengunduh Dataset**
Dataset link: https://drive.google.com/file/d/1HEBP8P5jsC2ghrkwaa5vk59iDqXaSWbv/view?usp=sharing
"""

# mengunduh dataset
gdd.download_file_from_google_drive(file_id='1HEBP8P5jsC2ghrkwaa5vk59iDqXaSWbv',
                                    dest_path='content/Crop_prediction.zip',
                                    unzip=True)

"""# **3.** ***Data Understanding***

### **3.1** ***Data Loading***
"""

# membaca dataset
data_path = "/content/content/Crop_prediction/Crop_prediction.csv"
dataset = pd.read_csv(data_path)
dataset

"""**Observasi :** <br>
Output kode di atas memberikan informasi sebagai berikut:

*   Terdapat 2200 baris (records atau jumlah pengamatan) dalam dataset.
*   Terdapat 8 kolom yaitu: N, P, K, temperature, humidity, ph, rainfall, label.
"""

label = dataset["label"].drop_duplicates().values
label

"""### **3.2** ***Exploratory Data Analysis*** **- Deskripsi Variabel**

**Deskripsi Variabel :** <br>
Berdasarkan informasi dari Kaggle, variabel-variabel pada Crop dataset adalah sebagai berikut:

1. N - rasio kandungan Nitrogen dalam tanah
2. P - rasio kandungan Fosfor dalam tanah
3. K - rasio kandungan Kalium dalam tanah
4. temperature - suhu dalam derajat Celcius
5. humidity - kelembaban relatif dalam %
6. ph - nilai ph tanah
7. rainfall - curah hujan dalam mm
8. label - label dari crop yang cocok untuk tumbuh di lahan pertanian berdasarkan variabel 1-7
"""

dataset.info()

"""**Observasi :** <br>
Output kode di atas memberikan informasi sebagai berikut:

* Terdapat 3 kolom numerik dengan tipe data int64, yaitu: N, P, K. Ini merupakan fitur numerik.
* Terdapat 4 kolom numerik dengan tipe data float64 yaitu: temperature, humidity, ph dan rainfall. Ini merupakan fitur numerik.
* Terdapat 1 kolom dengan tipe object, yaitu: label. Kolom ini merupakan categorical features (fitur non-numerik) dimana kolom ini merupakan target fitur.
"""

dataset.describe()

"""**Observasi :** <br>
Output kode di atas memberikan informasi statistik pada masing-masing kolom, antara lain:

* count  adalah jumlah sampel pada data.
* mean adalah nilai rata-rata.
* std adalah standar deviasi.
* min yaitu nilai minimum setiap kolom. 
* 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
* 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
* 75% adalah kuartil ketiga.
* Max adalah nilai maksimum.
"""

dataset.shape

"""### **3.3** ***Exploratory Data Analysis*** **- Memeriksa Missing Value**"""

# memeriksa apakah terdapat missing value pada dataset
dataset.isnull().sum()

"""**Observasi :** <br>
Output kode di atas memberikan informasi bahwa tidak terdapat *missing value* pada dataset.

### **3.4** ***Exploratory Data Analysis*** **- Univariate Analysis**

#### 3.4.1 Sebaran/distribusi data pada setiap fitur numerik
"""

#visualisasi data masing-masing fitur menggunakan histogram plot untuk mengetahui sebaran/distribusi data pada setiap fitur
features = dataset.columns[:-1]
for feature in features:
  figures = px.histogram(data_frame=dataset,
                        x=feature,
                        template='plotly_white',
                        marginal='box',
                        nbins=200,
                        color_discrete_sequence=["green"],
                        barmode='stack',
                        histfunc='count')

  title = "Sebaran/distribusi data pada fitur " + feature
  figures.update_layout(font_family='Open Sans',
                        title=dict(text=title, x=0.47, font=dict(color="#333",size=20)),
                        hoverlabel=dict(bgcolor='white'))

  figures.show()

"""**Observasi :** <br>
Berdasarkan hasil visualisasi data diatas, dapat terlihat sebaran atau distribusi data yang ada pada setiap fitur. Termasuk nilai minimum, median, maksimum, Q1, Q3, batas atas dan batas bawah. Selain itu dapat dilihat juga pada beberapa fitur masih terdapat nilai outliers.

#### 3.4.2 Sebaran/distribusi data pada fitur target
"""

#visualisasi data untuk mengetahui sebaran/distribusi data pada fitur target 'label'
plt.figure(figsize=(19,7))
sns.countplot(dataset['label'] , palette = 'Spectral')
plt.xticks(rotation=90)
plt.title("Sebaran/distribusi data pada fitur target (label)", fontdict= {'fontsize':18})
plt.show()

"""**Observasi :** <br>
Berdasarkan hasil visualisasi dari fitur target 'label' dapat memberikan informasi bahwa dataset sudah seimbang dengan jumlah sampel masing-masing label yaitu 100 sampel, sehingga tidak perlu menyeimbangkan data lagi.

### **3.5** ***Exploratory Data Analysis*** **- Multivariate Analysis**

#### 3.5.1 Mengecek dan Membandingkan rata rata kandungan fitur N, P, K antar label
"""

crop_summary = pd.pivot_table(dataset, index=['label'],aggfunc='mean')

# visualisasi kandungan N, P, K terhadap setiap label
for feature in features[:3]:
    plt.figure(figsize=(19,7))
    sns.barplot(x = "label", y = feature, data = dataset)
    plt.xticks(rotation=90)
    plt.title(f"Rata-rata {feature} terhadap label crop")
    plt.show()

    crop_summary_feature = crop_summary.sort_values(by=feature, ascending=False)
  
    fig = make_subplots(rows=1, cols=2)

    top = {
        'y' : crop_summary_feature[feature][0:11].sort_values().index,
        'x' : crop_summary_feature[feature][0:11].sort_values()
    }

    last = {
        'y' : crop_summary_feature[feature][-11:].index,
        'x' : crop_summary_feature[feature][-11:]
    }

    fig.add_trace(
        go.Bar(top,
              name="crop label dengan kandungan " + feature + " tinggi",
              marker_color='green',
              orientation='h',
              text=top['x']),
        
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(last,
              name="crop label dengan kandungan " + feature + " rendah",
              marker_color='red',
              orientation='h',
              text=last['x']),
        row=1, col=2
    )


    fig.update_traces(texttemplate='%{text}', textposition='inside')
    fig.update_layout(title_text=feature,
                      plot_bgcolor='white',
                      font_size=12, 
                      font_color='black',
                    height=500)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.show()

# visualisasi perbandingan kandungan fitur N, P, K antar label
fig = go.Figure()
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['N'],
    name='N',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['P'],
    name='P',
    marker_color='lightsalmon'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['K'],
    name='K',
    marker_color='crimson'
))

fig.update_layout(title="Perbandingan kandungan N, P, K antar label",
                  plot_bgcolor='white',
                  barmode='group',
                  xaxis_tickangle=-45)

fig.show()

"""**Observasi :** <br>
Hasil visualisasi di atas memberikan informasi mengenai rata-rata kandungan N, P, K terhadap setiap label crop. Dimana dapat dilihat bahwa terdapat beberapa label crop yang membutuhkan lahan dengan kandungan N,P,K tinggi dan beberapa label membutuhkan lahan dengan kandungan N,P,K rendah.

#### 3.5.2 Mengecek dan Membandingkan rata rata tingkat temperature, humidity dan rainfall antar setiap label
"""

# visualisasi tingkat temperature, humidity dan rainfall terhadap setiap label
features1 = features.delete(5)
for feature in features1[-3:]:
    plt.figure(figsize=(19,7))
    sns.barplot(x = "label", y = feature, data = dataset)
    plt.xticks(rotation=90)
    plt.title(f"Rata-rata tingkat {feature} terhadap label crop")
    plt.show()

    crop_summary_feature = crop_summary.sort_values(by=feature, ascending=False)
  
    fig = make_subplots(rows=1, cols=2)

    top = {
        'y' : crop_summary_feature[feature][0:11].sort_values().index,
        'x' : crop_summary_feature[feature][0:11].sort_values()
    }

    last = {
        'y' : crop_summary_feature[feature][-11:].index,
        'x' : crop_summary_feature[feature][-11:]
    }

    fig.add_trace(
        go.Bar(top,
              name="crop label dengan tingkat " + feature + " tinggi",
              marker_color='green',
              orientation='h',
              text=top['x']),
        
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(last,
              name="crop label dengan tingkat " + feature + " rendah",
              marker_color='red',
              orientation='h',
              text=last['x']),
        row=1, col=2
    )


    fig.update_traces(texttemplate='%{text}', textposition='inside')
    fig.update_layout(title_text=feature,
                      plot_bgcolor='white',
                      font_size=12, 
                      font_color='black',
                    height=500)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.show()

# visualisasi perbandingan tingkat temperature, humidity dan rainfall antar setiap label
fig = go.Figure()
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['temperature'],
    name='tepmerature',
    marker_color='coral'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['humidity'],
    name='humidity',
    marker_color='maroon'
))

fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['rainfall'],
    name='rainfall',
    marker_color='orangered'
))

fig.update_layout(title="Perbandingan tingkat temperature, humidity dan rainfall antar label",
                  plot_bgcolor='white',
                  barmode='group',
                  xaxis_tickangle=-45)

fig.show()

"""**Observasi :** <br>
Hasil visualisasi di atas memberikan informasi mengenai tingkat temperature, humidity dan rainfall terhadap setiap label crop. Dimana dapat dilihat bahwa terdapat beberapa label crop yang membutuhkan lahan dengan tingkat temperature, humidity dan rainfall tinggi dan beberapa label membutuhkan lahan dengan tingkat temperature, humidity dan rainfall rendah.

#### 3.5.5 Korelasi antar fitur numerik
"""

# korelasi antar fitur numerik menggunakan fungsi pairplot
plt.figure(figsize=(19,17))
sns.pairplot(dataset, hue = "label")
plt.show()

# korelasi antara fitur numerik menggunakan fungsi corr()
plt.figure(figsize = (13,11))
sns.heatmap(dataset.corr(), center = 0, annot = True)
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)
plt.show()

"""**Observasi :** <br>
Kode di atas memberikan informasi mengenai korelasi antara fitur numerik, dimana dari Correlation Matrix dapat dilihat bahwa fitur P dan K memiliki korelasi yang sedikit tinggi.

# **4.** ***Data Preparation***

### **4.1 Melakukan label encoding pada fitur target (label)**
"""

# memisahkan dataset menjadi data X (variabel independen) dan data y (variabel dependen)
# mengubah value pada fitur target 'label' dari kategorik menjadi numerik menggunakan LabelEncoder()
label_encoder = LabelEncoder()
X = dataset[features]
y = label_encoder.fit_transform(dataset["label"])

label_dict = {}
for i in range(22):
    label_dict[i] = label_encoder.inverse_transform([i])[0]
label_dict

"""**Observasi :** <br>
Sebelum masuk ke tahap pembagian dataset, terlabih dahulu melakukan pemisahan antara variabel independen (N, P, K, temperature, humidity, ph, rainfall) sebagai data X dan variabel dependen (label) sebagai data y. Karena fitur label pada dataset merupakan fitur non-numerik yang berarti nilai pada fitur tersebut adalah kategorikal, maka sebelum dimasukan ke dalam data y telah dilakukan proses label encoding untuk fitur tersebut. Label encoding merupakan teknik untuk mengubah jenis data kategorikal menjadi data numerik yang dapat dipahami model.

### **4.2 Melakukan pembagian data pada dataset**
"""

# melakukan pembagian data X dan y dengan train_test_split
X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size = 0.2, random_state = 0)
print(f'Total jumlah sample pada dataset: {len(X)}')
print(f'Total jumlah sample pada train dataset: {len(X_train)}')
print(f'Total jumlah sample pada test dataset: {len(X_test)}')

"""**Observasi :** <br>
Pembagian dataset dilakukan dengan presentase 80% data latih dan 20% data uji, dimana jumlah sampel pada data train yaitu 1760 sampel dan jumlah sampel pada data test yaitu 440 sampel.

### **4.3 Mengatasi Outliers pada data train dengan metode LOF _(Local Outlier Factor)_**
"""

# mengatasi outlier fungsi LocalOutlierFactor
lof = LocalOutlierFactor().fit_predict(X_train)
mask = lof != -1
X_train, y_train = X_train[mask, :], y_train[mask]

# mengecek shape dari data train setelah menghilangkan outlier
X_train.shape

"""**Observasi :** <br>
Data pencilan (outliers) merupakan nilai yang tidak normal pada dataset. Adanya data outliers ini akan membuat analisis terhadap serangkaian data menjadi bias, atau tidak mencerminkan fenomena yang sebenarnya sehingga dapat menyebabkan pada pembuatan model menjadi kurang optimal. Oleh karena itu, untuk menangani ouliers pada proyek ini menerapkan metode Local Outlier Factor untuk mengidentifikasi outliers dan kemudian menghapusnya dari data train, sehingga jumlah sampelnya menjadi 1758 sampel.

### **4.4 Standarisasi data pada fitur numerik**
"""

# melakukan standarisasi dengan fungsi StandardScaler()
scaler = StandardScaler()
scaler.fit(X_train)
scaler.fit(X_test)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

X_train

X_test

"""**Observasi :** <br>
Setelah dilakukan standarisasi data, dapat dilihat bahwa semua nilai dari fitur numerik pada data train dan data test berada dalam skala data yang sama.

# **5.** ***Model Development***

### **5.1** ***Model Development - K-Nearest Neighbor***
"""

# mencari nilai k yang optimal
error_rate = []
for i in range(1, 30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    knn_predictions = knn.predict(X_test)
    accuracy = accuracy_score(y_test, knn_predictions)
    print(f"Accuracy at k = {i} is {accuracy}")
    error_rate.append(np.mean(knn_predictions != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,30),error_rate,color='blue', linestyle='dashed', 
         marker='o',markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. Nilai K')
plt.xlabel('K')
plt.ylabel('Error Rate')

# didapatkan nilai k optimal adalah 1
print("Minimum error:-",min(error_rate)," pada K =",error_rate.index(min(error_rate))+1)

# membuat model dengan algoritma KKN
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# menguji model menggunakan data test
knn_predictions = knn.predict(X_test)
knn_report = classification_report(y_test, knn_predictions, output_dict=True, target_names=label)
pd.DataFrame(knn_report).transpose()

"""**Observasi :** <br>
Dari code di atas dapat dilihat bahwa model dengan algoritma K-Nearest Neighbor memperoleh nilai akurasi yaitu sebesar 0.979545 dengan k = 1

### **5.2** ***Model Development - Random Forest***
"""

# membuat model dengan algoritma Random Forest
rf = RandomForestClassifier(random_state = 18)
rf.fit(X_train, y_train)

# menguji model menggunakan data test
rf_predictions = rf.predict(X_test)
rf_report = classification_report(y_test, rf_predictions, output_dict=True, target_names=label)
pd.DataFrame(rf_report).transpose()

"""**Observasi :** <br>
Dari code di atas dapat dilihat bahwa model dengan algoritma Random Forest memperoleh nilai akurasi yaitu sebesar 0.997727

### **5.3** ***Model Development - XGBoost Algorithm***
"""

# membuat model dengan algoritma XGBoost
xgb = XGBClassifier(random_state = 18)
xgb.fit(X_train, y_train)

# menguji model menggunakan data test
xgb_predictions = xgb.predict(X_test)
xgb_report = classification_report(y_test, xgb_predictions, output_dict=True, target_names=label)
pd.DataFrame(xgb_report).transpose()

"""**Observasi :** <br>
Dari code di atas dapat dilihat bahwa model dengan algoritma XGBoost memperoleh nilai akurasi yaitu sebesar 0.995455

# **6. Evaluasi Model**

### **6.1** ***Confusion Matrix - K-Nearest Neighbor***
"""

plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(y_test, knn_predictions), annot = True)
plt.title("Confusion Matrix Model K-Nearest Neighbor")
plt.show()

"""### **6.2** ***Confusion Matrix - Random Forest***"""

plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(y_test, rf_predictions), annot = True)
plt.title("Confusion Matrix Model Random Forest")
plt.show()

"""### **6.3** ***Confusion Matrix - XGBoost Algorithm***"""

plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(y_test, xgb_predictions), annot = True)
plt.title("Confusion Matrix Model XGBoost Algorithm")
plt.show()

"""### **6.4 Perbandingan Metriks Accuracy antar Model**"""

#menghitung nilai akurasi, precision dan recall setiap model
knn_accuracy = round((accuracy_score(y_test, knn_predictions)*100), 2)
rf_accuracy = round((accuracy_score(y_test, rf_predictions)*100), 2)
xgb_accuracy = round((accuracy_score(y_test, xgb_predictions)*100), 2)

knn_precision = round((precision_score(y_test, knn_predictions, average='macro')*100), 2)
rf_precision = round((precision_score(y_test, rf_predictions, average='macro')*100), 2)
xgb_precision = round((precision_score(y_test, xgb_predictions, average='macro')*100), 2)

knn_recall = round((recall_score(y_test, knn_predictions, average='macro')*100), 2)
rf_recall = round((recall_score(y_test, rf_predictions, average='macro')*100), 2)
xgb_recall = round((recall_score(y_test, xgb_predictions, average='macro')*100), 2)

# membat dataframe hasil evaluasi
list_evaluasi= [[knn_accuracy, knn_precision, knn_recall],
            [rf_accuracy, rf_precision, rf_recall],
            [xgb_accuracy, xgb_precision, xgb_recall]]
evaluasi = pd.DataFrame(list_evaluasi,
                        columns=['Accuracy (%)', 'Precision (%)', 'Recall (%)'],
                        index=['K-Nearest Neighbor', 'Random Forest', 'XGBoost'])
evaluasi

"""**Observasi :** <br>
Dari hasil evaluasi di atas dapat memberikan informasi bahwa ketiga model yang dibangun memiliki performa di atas 80%. Dimana dapat dilihat juga bahwa model dengan algoritma Random Forest memiliki performa (nilai akurasi, precision, recall, dan F1 score) yang lebih baik dari dua model lainnya yaitu model dengan algoritma K-Nearest Neighbor dan XGBoost.

# **Penutup**

Model untuk memprediksi jenis tanaman yang cocok ditanam di lahan pertanian tertentu telah selesai dibuat dan dari hasil pengujian, ketiga model yang dibuat memiliki performa yang baik dan dapat digunakan untuk memprediksi data sebenarnya.


### *Referensi*
- https://www.kaggle.com/harshavarshney/crop-recommendation#EXPLORATORY-DATA-ANALYSIS
- https://www.kaggle.com/venugopalkadamba/croprecommendation-eda-visualization-modeling-99#XGBoost-Classifier
- https://www.kaggle.com/njain5/crop-prediction-using-classification-models
- https://towardsdatascience.com/beginners-guide-to-xgboost-for-classification-problems-50f75aac5390
- https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826
"""