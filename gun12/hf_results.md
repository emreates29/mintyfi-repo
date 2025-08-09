## Text Classification Sonuçları

Sonuçlar CPU kullanılarak elde edilmiştir

> **Not:** GPU kullanımı denendi ancak mevcut Python sürümünün (3.13) PyTorch'un CUDA destekli versiyonunu desteklememesi nedeniyle GPU üzerinde inference yapılamadı.  
> GPU hızlandırma için Python 3.11 veya 3.10 sürümlerinden birine geçiş yapmayı denedim ancak farklı kurulum ve uyumluluk hataları nedeniyle çalıştıramadım.  



| Girdi                               | Çıktı etiketi   |   Olasılık |   Süre |
|:------------------------------------|:----------------|-----------:|-------:|
| I really like this new phone.       | POSITIVE        |     0.9996 | 0.0287 |
| The food at the restaurant was bad. | NEGATIVE        |     0.9998 | 0.0316 |
| Technology is changing the world.   | POSITIVE        |     0.9996 | 0.0195 |




