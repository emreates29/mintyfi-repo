import pandas as pd
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("http://localhost:5000")

df = pd.read_csv('sms_clean.csv', encoding='utf-8')

X = df['mesaj']
y = df['etiket']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

max_features_values = [1000, 2000, 3000, None]
ngram = (1, 1)

best_accuracy = 0.0
best_run_id = None
best_params = {}

accuracies = []  

for max_features in max_features_values:
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=ngram, max_features=max_features)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(C=100.0, max_iter=200)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)  

    with mlflow.start_run() as run:
        mlflow.log_param("ngram_range", ngram)
        mlflow.log_param("C", 100.0)
        mlflow.log_param("max_features", max_features)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        print(f"Run ID: {run.info.run_id}, Accuracy: {acc:.4f}")

        if acc > best_accuracy:
            best_accuracy = acc
            best_run_id = run.info.run_id
            best_params = {
                "max_features": max_features,
                "accuracy": acc,
                "run_id": run.info.run_id,
                "model_uri": f"runs:/{run.info.run_id}/model"
            }

with open("best_run.txt", "w") as f:
    f.write(best_run_id)

with open("exp_notes.md", "w", encoding="utf-8") as f:
    f.write("# Deney Özeti\n")
    f.write(f"- **Run ID**: `{best_run_id}`\n")
    f.write(f"- **En iyi doğruluk**: `{best_accuracy:.4f}`\n")
    f.write(f"- **max_features**: `{best_params['max_features']}`\n")
    f.write(f"- **Model artifact URI**: `{best_params['model_uri']}`\n")

max_feats_for_plot = [mf if mf is not None else 0 for mf in max_features_values]
plt.figure(figsize=(8,5))
plt.plot(max_feats_for_plot, accuracies, marker='o')
plt.title('Max Features vs Accuracy')
plt.xlabel('max_features (0=None)')
plt.ylabel('Accuracy')
plt.grid(True)

plt.savefig("accuracy_plot.png")

with mlflow.start_run():
    mlflow.log_artifact("accuracy_plot.png")

plt.show()
