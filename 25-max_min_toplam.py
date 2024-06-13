"""
    Kullanıcıdan alınan 5 sayıdan en büyük ve en küçüğünün toplamını ekrana yazdırma
"""


# Boş bir liste oluşturuyorum
liste = []
topla = 0

# Kullanıcıdan 5 sayı almak için for döngüsü oluşturuyorum
for _ in range(5):
    sayi = int(input("Sayı: "))
    liste.append(sayi)
    topla+=sayi

print(f"En büyük sayı: {max(liste)}, En küçük sayı: {min(liste)}'dir. Bu sayıların toplamı: {topla}")
