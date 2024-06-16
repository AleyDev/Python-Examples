"""
    Kullanıcıdan aldığı metindeki tüm boşluk karakterlerini kaldırır.
    Girilen metni temiz bir şekilde ekrana yazdırır.
"""

# Boşlukları kaldırma fonksiyonunu tanımlıyorum
def bosluklari_kaldir(metin):
    # Girilen metindeki tüm boşluk karakterlerini boş string ile değiştiriyorum
    return metin.replace(" ", "")

# Kullanıcıdan bir metin girmesini istiyorum
metin = input("Metni girin: ")

# Boşlukları kaldırma fonksiyonunu çağırarak sonucu ekrana yazdırıyorum
print(f"Boşluklar çıkarıldıktan sonra: {bosluklari_kaldir(metin)}")
