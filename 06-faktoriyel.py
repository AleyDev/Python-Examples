"""
    Klavyeden girilen bir değerin faktöriyelini hesapla.
"""


# Kullanıcıdan bir sayı al
sayi = int(input("Lütfen bir sayı girin: "))

# Faktöriyel hesapla
faktoriyel = 1
# 1'den kullanıcınınn girdiği sayıya kadar olan sayılar için döngü oluştur.
for i in range(1, sayi + 1):
    # Her sayıyı faktöriyel değeri ile çarp
    faktoriyel *= i
"""
while sayi > 0: # while döngüsü ile
    faktoriyel = faktoriyel * sayi
    sayi -= 1"""

# Hesaplanan faktöriyel değerini ekrana yazdır
print("Girdiğiniz sayının faktöriyeli:", faktoriyel)
