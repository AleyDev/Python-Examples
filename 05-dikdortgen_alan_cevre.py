"""
    Dikdörtgenin alanı ve çevresi
"""


# Kullanıcıdan kısa kenar ve uzun kenar uzunluklarını girmesini iste
kisa_kenar = int(input("Kısa kenar: "))
uzun_kenar = int(input("Uzun kenar: "))

# Dikdörtgenin alanını hesapla (alan = kısa kenar * uzun kenar)
alan = kisa_kenar * uzun_kenar

# Dikdörtgenin çevresini hesapla (çevre = 2 * (kısa kenar + uzun kenar))
cevre = 2 * (kisa_kenar + uzun_kenar)

# Hesaplanan alan ve çevre değerlerini ekrana yazdır
print("Alanı: {}".format(alan), "\nÇevresi: {}".format(cevre))




"""
    Not: 
    'format()' fonksiyonu, alan ve çevre değerlerini belirtilen yerlerde yazdırmak için kullanılır.
"""