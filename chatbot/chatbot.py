import os
import fitz  
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import subprocess


PDF_PATH = "nutuk.pdf"
CACHE_PATH = "embeddings.pkl"
EMBED_MODEL = "intfloat/multilingual-e5-base"

TOP_K_CHUNKS = 3
MAX_TOKENS_CONTEXT = 400



def pdf_yukle(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            page_text = page.get_text()
            page_text = " ".join(page_text.split())
            text += page_text + " "
        doc.close()
        print(f"PDF '{path}' başarıyla yüklendi.")
        return text
    except Exception as e:
        print(f"Hata: PDF yüklenirken sorun oluştu: {e}")
        return ""


def metni_parcala(text, chunk_size=400, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    print(f"Metin {len(chunks)} parçaya ayrıldı.")
    return chunks


def embeddingleri_hazirla():
    if os.path.exists(CACHE_PATH):
        try:
            with open(CACHE_PATH, "rb") as f:
                print(f"Embeddingler '{CACHE_PATH}' dosyasından yükleniyor...")
                return pickle.load(f)
        except Exception as e:
            print(f"Hata: Cache yüklenemedi ({e}). Yeniden oluşturuluyor.")
            os.remove(CACHE_PATH)

    print("Embeddingler oluşturuluyor, biraz sürebilir...")
    text = pdf_yukle(PDF_PATH)
    if not text:
        return {"chunks": [], "embeddings": np.array([])}

    chunks = metni_parcala(text)
    try:
        model = SentenceTransformer(EMBED_MODEL)
        embeddings = model.encode(chunks, batch_size=32, show_progress_bar=True)
        data = {"chunks": chunks, "embeddings": embeddings}
        with open(CACHE_PATH, "wb") as f:
            pickle.dump(data, f)
        print("Embeddingler kaydedildi.")
        return data
    except Exception as e:
        print(f"Embedding oluşturulurken hata: {e}")
        return {"chunks": [], "embeddings": np.array([])}


def alakali_parcalari_bul(soru, data, top_k=TOP_K_CHUNKS, max_tokens=MAX_TOKENS_CONTEXT):
    if not data or not data["embeddings"].shape[0]:
        return []

    embed_model = SentenceTransformer(EMBED_MODEL)
    q_emb = embed_model.encode([soru])
    sims = cosine_similarity(q_emb, data["embeddings"])[0]
    idxs = np.argsort(sims)[::-1][:top_k]

    selected_chunks = []
    token_count = 0
    for i in idxs:
        chunk = data["chunks"][i]
        chunk_tokens_estimate = len(chunk.split())
        if token_count + chunk_tokens_estimate <= max_tokens:
            selected_chunks.append(chunk)
            token_count += chunk_tokens_estimate
        else:
            break
    return selected_chunks


def ollama_ile_sor(soru, context):
    system_msg = "Sen Atatürk’ün Nutuk eseri üzerine eğitimli bir asistansın. Sadece Nutuk’taki bilgilerle cevap ver. Cevap kısa ve net olsun, gereksiz açıklama ekleme. Tarih soruluyorsa **gün-ay-yıl formatında** yaz."
    user_msg = f"Soru: {soru}\nNutuk'tan ilgili kısımlar: {context}\nCevap:"

    full_prompt = f"{system_msg}\n{user_msg}"

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", full_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Ollama isteğinde hata: {e.stderr}"


def terminal_chat(data):
    print("Nutuk Chatbot'a hoş geldiniz! Soru yazın (çıkmak için 'q'):")
    while True:
        q = input("Soru: ")
        if q.strip().lower() == "q":
            print("Görüşmek üzere!")
            break
        if not q.strip():
            continue
        relevant = alakali_parcalari_bul(q, data)
        context = " ".join(relevant)
        answer = ollama_ile_sor(q, context)
        print("Cevap:", answer)
        print("-" * 80)


if __name__ == "__main__":
    data = embeddingleri_hazirla()
    terminal_chat(data)
