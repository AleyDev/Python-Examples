"""
    Klavyeden girilen n sayısına göre 1 den n ye kadar olan tek sayıların toplamı ve çarpımı, çift sayıların karelerinin toplamını yazdır.
"""


# Kullanıcıdan bir sayı al
sayi = int(input("Lütfen bir sayı giriniz: "))

# toplam, çarpım, kare değişkenlerini tanımla ve başlangıç değerlerni ata
toplam = 0
carpim = 1
kare = 0

# Eğer sayi tekse
if sayi % 2 == 1:
    # 1'den sayıya kadar olan sayılar için döngü
    for i in range(1, sayi + 1):
        # Her sayıyı toplam değişkenine ekle
        toplam = toplam + i
        # Her sayıyı çarpim değişkenine çarp
        carpim = carpim * i
else:  # Eğer sayı çiftse
    # 1'den sayıya kadar olan sayılar için döngü
    for i in range(1, sayi + 1):
        # Her sayının karesini kare değişkenine ekle
        kare = kare + i ** 2

# Sonuçları yazdır
if sayi % 2 == 1:
    print("1'den", sayi, "sayısına kadar olan sayıların toplamı: ", toplam)
    print("1'den", sayi, "sayısına kadar olan sayıların çarpımı: ", carpim)
else:
    print("1'den", sayi, "sayısına kadar olan sayıların karelerinin toplamı: ", kare)

