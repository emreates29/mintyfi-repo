import sys
import joblib


if len(sys.argv) != 2:
    print("kullqanım: python predict.py \"mesaj metni\"")
    sys.exit(1)

mesaj = sys.argv[1]


model = joblib.load("en_iyi_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


X = vectorizer.transform([mesaj])
tahmin = model.predict(X)[0]

etiket_cevir = {
    "spam": "reklam",
    "ham": "normal"
}

print("Tahmin:", etiket_cevir.get(tahmin, tahmin))
