"""
    Bir sayının pozitif, negatif veya sıfıra eşit olma durumu
"""


sayi = float(input("Sayı: "))  # Kullanıcıdan bir sayı girişi al

# Sayının durumunu kontrol et
if sayi == 0:
    print("Girilen sayı sıfıra eşittir.")
elif sayi > 0:
    print("Sayı pozitiftir.")
else:
    print("Sayı negatiftir.")
