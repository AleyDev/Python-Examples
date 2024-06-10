"""
    Maaş bilgisine ve çocouk sayısına göre yardım ücretini hesapla.
    Çocuk sayısı:
                 1 ise maaşın %5'i
                 2 ise maaşın %10'u
                 3 ve daha fazla ise maaşın %15'i
"""


# Kullanıcıdan maaş bilgisini al
maas_bilgisi = int(input("Lütfen maaş bilginizi giriniz: "))

# Kullanıcıdan çocuk sayısını al
cocuk_sayisi = int(input("Lütfen çocuk sayısını giriniz: "))

# Yardım parasını için bir değişken tanımla
yardim_parasi = 0

# Çocuk sayısına göre yardım ücretini hesapla
if cocuk_sayisi == 1:
    yardim_parasi = maas_bilgisi * 0.05
elif cocuk_sayisi == 2:
    yardim_parasi = maas_bilgisi * 0.10
elif cocuk_sayisi >= 3:
    yardim_parasi = maas_bilgisi * 0.15
else:
    print("Hatalı işlem! Çocuk sayısı 0 olamaz veya belirlenen aralık dışında.")

# Eğer yardım parası hesaplanmışsa, ekrana yazdır
if yardim_parasi > 0:
    print("Yardım ücretiniz:", yardim_parasi)
