"""
    Kullanıcıdan 5 sayı al ve bu sayıların toplamını ve ortalamasını ekrana yazdır
"""


sayac = 0
toplam = 0

for i in range(5):  # Döngüyü 5 kez çalıştırmak için range(5) kullanılmalı
    x = int(input("Sayı Giriniz: "))  # Döngü her seferinde kullanıcıdan bir sayı isteyecek
    toplam = toplam + x  # Toplamı güncellemek için her seferinde x'i eklemek gerekir
    sayac = sayac + 1  # Sayacın döngü her seferinde artırılması gerekir

ort = toplam / sayac  # Ortalamanın hesaplanması döngünün dışında olmalı

print("Toplam:", toplam)
print("Ortalama:", ort)
