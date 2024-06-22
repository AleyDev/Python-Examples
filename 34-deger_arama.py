"""
    Kullanıcıdan bir değer alıp, bu değerin listede olup olmadığını kontrol etme ve kullanıcıya bildirme
"""



# İçerisinde arama yapacağımız sayılardan oluşan bir liste
liste = [1, 2, 3, 4, 5, 6]

# Kullanıcıdan bir değer girmesini istiyoruz ve bu değeri 'deger' değişkenine atıyoruz.
deger = int(input("Aramak istediğiniz değeri girin: "))

# 'deger' değişkeninin 'liste' içinde olup olmadığını kontrol ediyoruz.
if deger in liste:
    # Eğer 'deger' 'liste' içinde bulunuyorsa, bu değerin indeksini buluyoruz.
    indis = liste.index(deger)
    # Bulunan indeksi kullanıcıya bildiriyoruz.
    print(f"Aranan değer {indis}. indekste bulundu.")
else:
    # Eğer 'deger' 'liste' içinde bulunmuyorsa, kullanıcıya değerin bulunamadığını bildiriyoruz.
    print("Aranan değer bulunamadı.")


"""
    Hata yönetimli hali:
"""

# Kullanıcıdan bir değer alıp, bu değerin listede olup olmadığını kontrol eder ve sonucu bildirir.

# Önceden tanımlı liste
liste = [1, 2, 3, 4, 5, 6]  # Arama yapacağımız sabit liste.

# Kullanıcıdan bir değer alma
try:
    # Kullanıcıdan aramak istediği değeri girmesini istiyoruz.
    deger = int(input("Lütfen aramak istediğiniz değeri girin: "))
except ValueError:
    # Kullanıcı sayı yerine geçersiz bir giriş (örneğin harf) yaparsa, bu blok çalışır.
    print("Geçersiz giriş! Lütfen bir sayı girin.")
else:
    # Eğer kullanıcı geçerli bir sayı girdiyse, bu blok çalışır.
    
    # Değerin listede olup olmadığını kontrol etme
    if deger in liste:
        # Eğer girilen değer listede varsa, bu değerin indeksini buluruz.
        indis = liste.index(deger)
        # Bulunan indeksi ve değeri kullanıcıya bildiririz.
        print(f"Aranan değer {deger}, listede {indis}. indekste bulundu.")
    else:
        # Eğer girilen değer listede yoksa, kullanıcıya değerin bulunamadığını bildiririz.
        print(f"Aranan değer {deger}, listede bulunamadı.")
