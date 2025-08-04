# AI Feedback Report

## Hangi AI önerileri işe yaradı?

- fastapi lifespan event handler ile model ve vectorizer yüklemesini yapmak iyi oldu, uygulama açılır açılmaz kaynaklar düzgün yüklendi
- kaynakları endpoint fonksiyonlarına geçirmek kodu daha kolay test etmeye ve yönetmeye yardımcı oldu
- test fonksiyonları yazmakta ai’den aldığım öneriler sayesinde hızlıca kapsamlı testler oluşturabildim

## Hangi AI önerilerine güvenmedim ?

- Bazen AI önerileri startup işlemlerini çok karmaşıklaştırıyordu, basit `lifespan` event yapısı daha uygundu.


## Genel izlenim

- ai destekli kod asistanları hızlıca başlangıç ve refactor kodu yazmak için çok faydalı oldu.
- yazılım geliştirmede ai kullanımının verimliliği artırdığını gösterdi, ama insan gözetimi halen şart.
