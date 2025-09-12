import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

DOSYA_YOLU = "uber.csv" 

def veri_yukle(yol):
    veri = pd.read_csv(yol)


    if "Date" in veri.columns and "Time" in veri.columns:
        veri["tarih_saat"] = pd.to_datetime(
            veri["Date"] + " " + veri["Time"], errors="coerce"
        )
        veri["saat"] = veri["tarih_saat"].dt.hour
        veri["gun"] = veri["tarih_saat"].dt.day_name()
        veri["ay"] = veri["tarih_saat"].dt.month

    return veri

def veri_temizle(veri):
    print("Eksik değer oranı sütunlara göre:")
    print(veri.isna().mean())

 
    for sutun in ["Booking Value", "Ride Distance", "Driver Ratings", "Customer Rating"]:
        if sutun in veri.columns:
            veri[sutun] = pd.to_numeric(veri[sutun], errors="coerce")
            veri[sutun] = veri[sutun].fillna(veri[sutun].median())

    return veri

def kesifsel_analiz(veri):
    if "Ride Distance" in veri.columns:
        plt.figure(figsize=(8,5))
        sns.histplot(veri["Ride Distance"], bins=30, kde=True)
        plt.title("Yolculuk Mesafesi Dağılımı")
        plt.xlabel("Mesafe (km)")
        plt.show()

def pano_metrikleri(veri):
    toplam_yolculuk = veri.shape[0]
    ort_ucret = veri["Booking Value"].mean() if "Booking Value" in veri.columns else None
    ort_mesafe = veri["Ride Distance"].mean() if "Ride Distance" in veri.columns else None
    en_yogun_saat = veri["saat"].value_counts().idxmax() if "saat" in veri.columns else None
    en_yogun_gun = veri["gun"].value_counts().idxmax() if "gun" in veri.columns else None

    print("\n Pano Metrikleri")
    print(f"Toplam Yolculuk: {toplam_yolculuk}")
    if ort_ucret: print(f"Ortalama Ücret: {ort_ucret:.2f}")
    if ort_mesafe: print(f"Ortalama Mesafe: {ort_mesafe:.2f} km")
    if en_yogun_saat is not None: print(f"En Yoğun Saat: {en_yogun_saat}")
    if en_yogun_gun: print(f"En Yoğun Gün: {en_yogun_gun}")

def model_egit(veri):

    if "Booking Status" not in veri.columns:
        print("Booking Status sütunu yok, model kurulamadı.")
        return

    hedef = veri["Booking Status"]
    ozellikler = ["Booking Value", "Ride Distance", "Driver Ratings", 
                  "Customer Rating", "saat", "ay", "Vehicle Type", "Payment Method"]

    X = veri[ozellikler].copy()

    for sutun in ["Vehicle Type", "Payment Method"]:
        if sutun in X.columns:
            le = LabelEncoder()
            X[sutun] = le.fit_transform(X[sutun].astype(str))

    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X, hedef, test_size=0.2, random_state=42)

   
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_tahmin = model.predict(X_test)

    print("\nModel Performansı (Booking Status Tahmini)")
    print(classification_report(y_test, y_tahmin, digits=3))  
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_tahmin))

if __name__ == "__main__":
    veri = veri_yukle(DOSYA_YOLU)
    veri = veri_temizle(veri)
    kesifsel_analiz(veri)
    pano_metrikleri(veri)
    model_egit(veri)
