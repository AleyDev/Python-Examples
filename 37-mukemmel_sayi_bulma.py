"""
    Mükemmel sayılar, kendileri hariç pozitif bölenlerinin toplamı kendilerine eşit olan sayılardır.
"""



# Kullanıcıdan sayı girişi alıyorum
sayi = int(input("Lütfen bir sayı girin: "))

# Mükemmel sayıyı bulmak için bir fonksiyon tanımlıyorum
def mukemmel_sayi_bul(sayi):
    toplam = 0
    # Sayının kendisi hariç pozitif bölenlerini kontrol ediyorum
    for i in range(1, sayi):
        # Eğer i sayıya tam bölünüyorsa, i'yi toplam değişkenine ekliyorum
        if sayi % i == 0:
            toplam += i
    
    # Toplam, sayıya eşitse sayı mükemmel sayıdır ve True döner
    if toplam == sayi:
        return True
    else:
        return False

# Kullanıcının girdiği sayı için mükemmel sayı fonksiyonunu çağırıyorum
if mukemmel_sayi_bul(sayi):
    print(f"{sayi} mükemmel bir sayıdır.")
else:
    print(f"{sayi} mükemmel bir sayı değildir.")
