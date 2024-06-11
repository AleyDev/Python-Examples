"""
    Üs alma işlemini yapan recursive fonksiyon
"""

def ustel(a, b):
    # Eğer üs (b) 0 ise, herhangi bir sayının 0. kuvveti 1 olduğu için 1 döndür.
    if b == 0:
        return 1
    else:
        # Üs 0 değilse, a ile a'nın (b-1) üssünün çarpımını döndür
        return a * ustel(a, b-1)

# Fonksiyonu 2^4 hesaplamak için çağır ve sonucu yazdır
print(ustel(2, 4))
