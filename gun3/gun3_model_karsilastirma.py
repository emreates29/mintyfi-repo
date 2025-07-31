import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

veri = pd.read_csv("sms_clean.csv")

X_egitim, X_test, y_egitim, y_test = train_test_split(
    veri["mesaj"], veri["etiket"],
    test_size=0.2,
    stratify=veri["etiket"],
    random_state=42
)

tfidf = TfidfVectorizer()
X_egitim_tfidf = tfidf.fit_transform(X_egitim)
X_test_tfidf = tfidf.transform(X_test)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "MultinomialNB": MultinomialNB(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_egitim_tfidf, y_egitim)
    preds = model.predict(X_test_tfidf)

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, preds),
        "Precision": precision_score(y_test, preds, pos_label='spam'),
        "Recall": recall_score(y_test, preds, pos_label='spam'),
        "F1 Score": f1_score(y_test, preds, pos_label='spam'),
        "Confusion Matrix": confusion_matrix(y_test, preds).tolist()
    })

results_df = pd.DataFrame(results).sort_values("F1 Score", ascending=False)
print(results_df)
