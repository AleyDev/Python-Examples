"""
    Sayı tahmin oyunu, kullanıcının bilgisayar tarafından rastgele seçilen bir sayıyı belirli bir tahmin hakkı içinde doğru tahmin etmeye çalıştığı basit bir tahmin oyunu.
"""


# Rastgele sayı üretmek için random modülünü dahil ediyorum
import random

# Tahmin oyunu adında fonksiyon tanımlıyorum
def tahmin_oyunu():
    # 1 ile 100 arasında rastgele bir sayı seçiyorum
    sayi = random.randint(1, 100)
    tahmin_hakki = 10  # Kullanıcının 10 tahmin hakkı var
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

    # Kullanıcı tahmin haklarını kullanırken bir döngü başlatıyorum
    while tahmin_hakki > 0:
        # Kullanıcıdan bir tahmin girmesini istiyorum
        tahmin = int(input("Tahmininizi girin: "))

        # Kullanıcının tahmini tutulan sayıdan küçükse
        if tahmin < sayi:
            print("Daha yüksek bir sayı girin.")
        # Kullanıcının tahmini tutulan sayıdan büyükse
        elif tahmin > sayi:
            print("Daha düşük bir sayı girin.")
        # Kullanıcı doğru tahmin ettiğinde
        else:
            print(f"Tebrikler! {10 - tahmin_hakki + 1} denemede bildiniz.")
            break
        
        # Her tahminden sonra kalan hakkı azaltıyorum
        tahmin_hakki -= 1
        print(f"Kalan tahmin hakkınız: {tahmin_hakki}")

    # Kullanıcı tahmin hakkı bittiğinde doğru tahmini yapamamışsa
    if tahmin_hakki == 0:
        print(f"Üzgünüm, bilemediniz. Tutulan sayı: {sayi}")

# Tahmin oyunu fonksiyonunu çağırıyorum
tahmin_oyunu()
