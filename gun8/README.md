# Meme Kanseri Teşhisi Sınıflandırma Projesi

## Proje Özeti
Proje Kanser veri seti kullanılarak meme kanserinin iyi huylu veya kötü huylu olarak sınıflandırılması içindir. 

---

## Veri Seti
- **Kaynak:** (https://datadryad.org/dataset/doi:10.5061/dryad.r1m19)  
- **Hedef Değişken:** `diagnosis` (0 = iyi huylu, 1 = kötü huylu)

---

## Problem Tanımı
 Hastaların tümörlerinin iyi veya kötü huylu olduğunu tahmin etmek

---

## Kullanılan Yöntemler
- Veri temizleme ve ön işleme (gereksiz sütunların çıkarılması, Label Encoding, standart ölçeklendirme)  
- Eğitim ve test setlerine ayırma (%70 eğitim, %30 test)  
- Modeller:  
  - Logistic Regression  
  - K-Nearest Neighbors  
  - Support Vector Machine  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
  - Naive Bayes  
  - XGBoost  
  - Extra Trees  
- Model performans değerlendirmesi: Accuracy, Precision, Recall, F1-score, Classification Report

---

## Sonuçlar

| Model                   | Doğruluk (Accuracy) |
|-------------------------|---------------------|
| Logistic Regression     | 0.97                |
| Random Forest           | 0.96                |
| XGBoost                | 0.97                |
| Support Vector Machine  | 0.95                |
| K-Nearest Neighbors     | 0.94                |
| Decision Tree           | 0.91                |
| Gradient Boosting       | 0.96                |
| Naive Bayes             | 0.93                |
| Extra Trees             | 0.96                |

