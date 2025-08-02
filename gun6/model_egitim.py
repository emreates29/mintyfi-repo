import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("veri.csv")

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, max_df=0.95)
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=300, solver='liblinear', class_weight='balanced')
model.fit(X_train_vect, y_train)

y_pred = model.predict(X_test_vect)
print("Sınıflandırma Raporu:\n")
print(classification_report(y_test, y_pred))

joblib.dump(model, "en_iyi_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model ve vectorizer kaydedildi.")
