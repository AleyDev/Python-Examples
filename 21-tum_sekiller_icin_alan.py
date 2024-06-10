"""
    Kare: alan = kenar ** 2
    Dikdörtgen: alan = uzunluk * genişlik
    Daire: alan = π * r ** 2
    Üçgen: alan = (taban * yükseklik) / 2
    Paralelkenar: alan = taban * yükseklik
"""


# math kütüphanesini dahil ettim
import math

# Fonksiyonları tanımlıyorum

# Kare alanı hesaplama fonksiyonu
def kare_alani():
    kenar = int(input("Karenin bir kenar uzunluğunu giriniz: "))
    alan = kenar ** 2
    print("Karenin alanı: ", alan)


# Dikdörtgen alanı hesaplama fonksiyonu
def dikdortgen_alani():
    uzunluk = float(input("Dikdörtgenin uzunluğunu giriniz: "))
    genislik = float(input("Dikdörtgenin genişliğini giriniz: "))
    alan = uzunluk * genislik
    print("Dikdörtgenin alanı: ", alan)


# Daire alanı hesaplama fonksiyonu
def daire_alani():
    yaricap = float(input("Dairenin yarıçapını giriniz: "))
    alan = math.pi * yaricap ** 2
    print("Dairenin alanı: ", alan)


# Üçgen alanı hesaplama fonksiyonu
def ucgen_alani():
    taban = float(input("Üçgenin taban uzunluğunu giriniz: "))
    yukseklik = float(input("Üçgenin yüksekliğini giriniz: "))
    alan = (taban * yukseklik) / 2
    print("Üçgenin alanı: ", alan)


# Paralelkenar alanı hesaplama fonksiyonu
def paralelkenar_alani():
    taban = float(input("Paralelkenarın taban uzunluğunu giriniz: "))
    yukseklik = float(input("Paralelkenarın yüksekliğini giriniz: "))
    alan = taban * yukseklik
    print("Paralelkenarın alanı: ", alan)

# Kullanıcıdan şekil seçimini ve gerekli bilgileri alarak alan hesaplama fonksiyonu
def alan_hesapla():
    print("Alanını hesaplamak istediğiniz şekli seçin:")
    print("1. Kare")
    print("2. Dikdörtgen")
    print("3. Daire")
    print("4. Üçgen")
    print("5. Paralelkenar")
    
    # Kullanıcıdan seçim alma
    secim = input("Seçiminiz (1/2/3/4/5): ")
    
    # Kullanıcının seçimine göre ilgili alan hesaplama fonksiyonunu çağırma
    if secim == '1':
        kare_alani()
    elif secim == '2':
        dikdortgen_alani()
    elif secim == '3':
        daire_alani()
    elif secim == '4':
        ucgen_alani()
    elif secim == '5':
        paralelkenar_alani()
    else:
        print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı giriniz.")

# Alan hesaplama fonksiyonunu çağırdım
alan_hesapla()
