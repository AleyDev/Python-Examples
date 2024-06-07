"""
    Kullanıcıdan alınan bir metni 10 kez yazdır.
"""


# 1 - while döngüsü ile:

# Kullanıcıdan bir metin girmesini iste
yazi = input("Lütfen bir metin giriniz: ")

# Sayaç değişkenini başlat
sayac = 0

# Sayaç 10'dan küçük olduğu sürece döngü devam eder
while sayac < 10:
    # Metni ekrana yazdır
    print(yazi)
    # Sayaç değişkenini 1 arttır
    sayac += 1


"""

# 2 - for döngüsü ile:

# Kullanıcıdan bir metin girmesini iste
yazi = input("Lütfen bir metin giriniz: ")

# 1'den 10'a kadar döngü oluştur
for i in range(1, 11):
    # Metni ekrana yazdır
    print(yazi)
    
"""