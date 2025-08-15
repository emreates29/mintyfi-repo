from transformers import pipeline

sentiment_model = pipeline("text-classification", model="final_imdb_model")

id2label = {0: "NEGATIVE", 1: "POSITIVE"}

test_sentences = [
    "This movie was absolutely fantastic!",
    "I really did not enjoy this movie at all.",
    "The plot was very predictable but the acting was good.",
    "What a waste of time, totally boring!",
    "I laughed so much, it was hilarious!"
]

for sentence in test_sentences:
    result = sentiment_model(sentence)[0]  
    label_index = int(result['label'].split('_')[1])  
    result_label = id2label[label_index]
    print(f"Text: {sentence}")
    print(f"Predicted label: {result_label}, Score: {result['score']:.4f}\n")
