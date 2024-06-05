"""
    Klavyeden girilen 10 adet sayıdan en büyük olanı bulup ekrana yazdır.
"""

 
# Kullanıcının gireceği sayı adedini saymak için sayaç tanımlıyoruz
sayac = 0

# İlk başta en büyük sayıyı 0 olarak kabul ediyoruz (negatif sayılar girebileceği durumu düşünerek en_buyuk_sayi başlangıçta çok küçük bir değer olmalı)
en_buyuk_sayi = float('-inf')

# Kullanıcıdan 10 adet sayı alacağız, bu yüzden while döngüsü 10 kez çalışacak
while sayac < 10:
    # Kullanıcıdan bir sayı alıyoruz
    sayi = int(input("Sayı giriniz: "))

    # Girilen sayının en büyük sayıdan büyük olup olmadığını kontrol ediyoruz
    if sayi > en_buyuk_sayi:
        # Eğer girilen sayı en büyük sayıdan büyükse, en büyük sayıyı güncelliyoruz
        en_buyuk_sayi = sayi
    
    # Sayacımızı 1 arttırıyoruz
    sayac += 1

# Döngü tamamlandıktan sonra en büyük sayıyı ekrana yazdırıyoruz
print("En büyük sayı: ", en_buyuk_sayi)
