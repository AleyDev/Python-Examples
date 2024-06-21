# 1. Liste elemanları içindeki sayısal değerleri bulma
liste = ["1","2","5a","10b","abc","10","50"]

for i in liste:
    try:
        result = int(i)  # Her bir öğeyi tamsayıya çevirmeye çalış
        print(result)    # Başarılıysa tamsayıyı ekrana yazdır
    except ValueError:
        continue          # ValueError hatası alırsan döngüyü devam ettir



# 2. Kullanıcıdan input alırken hata kontrolü
while True:
    sayi = input('sayı: ')
    if sayi == 'q':      # Kullanıcı 'q' girdiğinde döngüden çık
        break

    try:
        result = float(sayi)  # Gelen inputu float'a çevirmeye çalış
        print('girdiğiniz sayı ', result)  # Başarılıysa sayıyı ekrana yazdır
    except ValueError:
        print('geçersiz sayı: ')  # ValueError hatası alırsan geçersiz sayı mesajı ver



# 3. Türkçe karakter içeren parolaları kontrol etme
def checkPassword(parola):
    tr_karakterler = 'şçğüöıİ'
    
    for i in parola:
        if i in tr_karakterler:  # Parola içinde Türkçe karakter varsa
            raise TypeError('Parola türkçe karakter içeremez.')  # TypeError hatası fırlat
        else:
            pass  # Türkçe karakter yoksa geç

    print('geçerli parola')  # Türkçe karakter içermeyen parola durumunda bu mesajı yazdır

parola = input('parola: ')

try:
    checkPassword(parola)  # Parolayı kontrol et
except TypeError as err:
    print(err)  # Türkçe karakter içeriyorsa hatayı ekrana yazdır



# 4. Faktöriyel hesaplama işlemi ve hata kontrolü
def faktoriyel(x):
    x = int(x)  # Gelen değeri tamsayıya çevir

    if x < 0:  # Negatif bir değer ise
        raise ValueError('Negatif değer')  # ValueError hatası fırlat

    result = 1

    for i in range(1, x+1):
        result *= i  # Faktöriyel hesaplama

    return result  # Sonucu döndür



# Belli değerler için faktöriyel hesapla ve hata durumlarını kontrol et
for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)  # Negatif değer veya geçersiz input için hata mesajını yazdır
        continue
    print(y)  # Başarılı hesaplama durumunda faktöriyel sonucunu yazdır
