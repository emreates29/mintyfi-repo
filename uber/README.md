# Uber Ride Analytics & ML Model

Bu proje, **Uber veri seti** üzerinden yolculuk analizi ve **Booking Status tahmini** yapmak için hazırlanmıştır.

## 📂 Proje İçeriği

- `uber.py` : Veri temizleme, keşifsel analiz (EDA) ve ML modeli (Random Forest) ile Booking Status tahmini.
- `uber.csv` : Kaggle'dan alınan Uber veri seti (CSV formatında).
- `README.md` : Proje açıklaması ve kullanım rehberi.

## 📝 Veri Seti

Kullanılan veri seti: [Uber Ride Analytics Dashboard - Kaggle](https://www.kaggle.com/datasets/yashdevladdha/uber-ride-analytics-dashboard)

Sütunlar:

- `Date`, `Time` → Tarih ve saat bilgisi  
- `Booking ID`, `Booking Status`, `Customer ID` → Rezervasyon ve müşteri bilgisi  
- `Vehicle Type`, `Pickup Location`, `Drop Location` → Araç ve lokasyon bilgisi  
- `Avg VTAT`, `Avg CTAT` → Ortalama bekleme süreleri  
- `Cancelled Rides by Customer/Driver`, `Reason for cancelling...` → İptal bilgileri  
- `Incomplete Rides`, `Booking Value`, `Ride Distance`, `Driver Ratings`, `Customer Rating`, `Payment Method`  

## ⚙️ Kurulum

1. Sanal ortam oluştur ve aktif et:

```bash
# Sanal ortamın kurulup aktif edilmesi 
- python -m venv venv
- .\venv\Scripts\Activate.ps  # Windows PowerShell
#
# Gerekli paketleri yükle:
pip install pandas numpy matplotlib seaborn plotly scikit-learn
# Çalıştırma
- uber.py dosyasını çalıştır:
- python uber.py


## Model Performansı

Tahmin edilen sınıflar: Completed, Cancelled by Customer, Cancelled by Driver, Incomplete, No Driver Found

Precision, Recall, F1-score ve Accuracy ile değerlendirilir.

Dengesiz veri sınıflarında (az örnekli sınıflar) performans düşebilir.

## 🔧 Notlar

Eksik sayısal değerler median ile doldurulmuştur.

Date + Time sütunları birleştirilerek datetime oluşturulmuştur.

Kategorik sütunlar (Vehicle Type, Payment Method) label encoding ile sayısallaştırılmıştır.

## 🖥️ Sonuç

Model Performansı (Booking Status Tahmini)
                       precision    recall  f1-score   support

Cancelled by Customer      0.183     0.027     0.048      2077
  Cancelled by Driver      0.565     0.934     0.704      5431
            Completed      1.000     0.997     0.998     18642
           Incomplete      0.965     1.000     0.982      1752
      No Driver Found      0.217     0.033     0.058      2098

             accuracy                          0.851     30000
            macro avg      0.586     0.598     0.558     30000
         weighted avg      0.808     0.851     0.813     30000
