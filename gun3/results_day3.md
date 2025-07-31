# Gün 3 Model Karşılaştırma Sonuçları

### Modellerin Performansları

| Model               | Accuracy | Precision | Recall  | F1 Score | Confusion Matrix      |
|---------------------|----------|-----------|---------|----------|----------------------|
| Random Forest       | 0.970986 | 0.990291  | 0.778626| 0.871795 | [[902, 1], [29, 102]]|
| Logistic Regression | 0.964217 | 0.960784  | 0.748092| 0.841202 | [[899, 4], [33, 98]] |
| MultinomialNB       | 0.952611 | 1.000000  | 0.625954| 0.769953 | [[903, 0], [49, 82]] |



- **Random Forest**, en yüksek F1 skoruna (0.872) ulaştı. Spam mesajları diğer modellere göre daha iyi tespit ediyor.

- **Logistic Regression** modeli de iyi sonuçlar verdi ve Random Forest’a yakın performans sergiledi.

- **MultinomialNB** modeli precision konusunda mükemmel olsa da, bazı spam mesajları kaçırdığı için F1 skoru daha düşük kaldı.

- Genel olarak, spam tespiti için **Random Forest**  modeli en iyi seçenek gibi görünüyor.