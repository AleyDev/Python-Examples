"""
    Kullanıcıdan alınan bir metindeki kelime sayısını hesaplama ve ekrana yazdırma işlemi. Metindeki kelimeleri boşluk karakterlerine göre ayırır ve kelime sayısını bulur.
"""


# kelime_sayaci adında bir fonksiyon tanımlıyorum
def kelime_sayaci(metin):
    # Kullanıcının girdiği metni boşluklara göre ayırarak kelimeler listesi oluşturuyorum
    kelimeler = metin.split()
    # Kelimeler listesinin uzunluğunu döndürüyorum, yani kelime sayısını
    return len(kelimeler)

# Kullanıcıdan bir metin girmesini istiyorum
metin = input("Bir metin girin: ")
# Kullanıcının girdiği metindeki kelime sayısını hesaplamak için kelime_sayaci fonksiyonunu çağırıyorum
kelime_sayisi = kelime_sayaci(metin)
# Hesaplanan kelime sayısını ekrana yazdırıyorum
print(f"Metinde {kelime_sayisi} kelime var.")
