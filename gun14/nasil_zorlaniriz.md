# Gün 14

## Amaç  
**LLM/NLP kavram özetini yapmak** ve sonraki 15 günlük ileri faza hazırlık konularını toplamak.  

## 1️⃣ LLM / NLP Kavram Özetleri  

**Large Language Model (LLM)** ve **Natural Language Processing (NLP)**

### **Token**  
- LLM’lerin işlediği en küçük anlam birimi.  
- Kelime veya tek bir harf olabilir.  

### **Embedding**  
- Metinlerin sayısal vektörler olarak temsil edilmesi.  
- Benzer anlamdaki metinler embedding uzayında birbirine yakın yer alır.  
- Arama, benzerlik karşılaştırma, kümeleme gibi işlemlerde kullanılır.  

### **Context Penceresi**  
- Modelin tek seferde “hatırlayabileceği” token sayısı.  
- Pencere genişledikçe geçmiş konuşma daha uzun süre hatırlanır.  

### **Temperature**  
- Çıktıların rastgeleliğini kontrol eder.  
- **0** → Daha kararlı, her zaman en olası cevabı verir.  
- **1** → Daha yaratıcı, ancak bazen tutarsız cevaplar verebilir.  

### **Top-p** (nucleus sampling)  
- Modelin seçim yapacağı olasılık havuzunu sınırlar.  
- **top_p=0.9** → En olası %90’lık havuzdan seçim yapar, geri kalan olasılıkları dikkate almaz.  
- Temperature ile birlikte yaratıcı/kararlı dengeyi ayarlamak için kullanılır.  

---

## 2️⃣ Sonraki 15 Günlük İleri Faz Konuları  

1. **Prompt engineering** (rol, format, kısıtlama teknikleri).  
2. **RAG (Retrieval-Augmented Generation)** yapısı ve uygulaması.  
3. **Fine-tuning**: LoRA, PEFT, full fine-tune farkları.  
4. **Evaluation & Benchmarks**: LLM çıktı kalitesi ölçüm teknikleri.  
5. **LangChain / LlamaIndex** ile zincirleme sorgular.  
6. **Multi-modal modeller** (metin + görsel).  
7. **Tool kullanımı**: Kod çalıştırma, web arama, dosya okuma.  
---

## 3️⃣ Ödev: NLP’de Bizi En Çok Ne Zorlar?  

1. **Token sınırının dolması**  
   - Uzun metinlerde veya çok turlu konuşmalarda context penceresinin aşılması sonucu önceki bilgilerin unutulması.  

2. **Türkçe dil desteğinin sınırlı olması**  
   - Modellerin çoğu İngilizce ağırlıklı eğitildiği için Türkçe metinlerde anlam kaybı veya hatalı yanıtlar oluşması.  

3. **Embedding boyutu seçimi**  
   - Daha yüksek boyutlu embeddingler daha doğru olabilir ancak depolama, arama hızı ve maliyet dengesini zorlaştırır.  

4. **Hallucination (uydurma) problemi**  
   - Modelin güvenle ama yanlış bilgi üretmesi, özellikle doğrulama yapılmadığında fark edilmesi zor olabilir.  

5. **Hız / kalite dengesini kurmak**  
   - Daha büyük ve kaliteli modellerin cevap süresi uzar, küçük modeller ise bazen yetersiz kalır.  
