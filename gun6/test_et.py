import requests

texts = [
    "There is a meeting today at 5 PM.",
    "Congratulations! Click here to claim your prize.",
    "Don’t forget the class starts at 10 AM tomorrow."
]

with open("curl_logs.txt", "w", encoding="utf-8") as f:
    for text in texts:
        payload = {"text": text}
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        f.write(f"Input: {text}\n")
        f.write(f"Output: {result}\n\n")
