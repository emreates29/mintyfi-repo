import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


df = pd.read_csv("veri.csv")

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vect, y)

joblib.dump(model, "en_iyi_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("kaydedildi.")
