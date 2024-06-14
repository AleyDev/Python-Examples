# Matematiksel işlemler için fonksiyonları tanımlıyorum
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    # Bölme işlemi için ikinci sayının sıfır olmaması gerekiyor, bunu kontrol ediyorum
    if b == 0:
        print("\nBölme işlemi için ikinci sayı sıfır olamaz!")
        return None  # Hata durumunu belirtmek için None döndürüyorum
    else:
        return a / b  # Bölme işlemi gerçekleştiriliyor ve sonuç döndürülüyor

# Kullanıcıya işlem seçeneklerini gösteriyorum
while True:
    print("\nYapmak istediğiniz işlemi seçiniz (1-4): ")
    print("1. Toplama işlemi")
    print("2. Çıkarma işlemi")
    print("3. Çarpma işlemi")
    print("4. Bölme işlemi")
    print("Çıkmak için q")

    # Kullanıcıdan işlem seçimini alıyorum
    secim = input("\nSeçiminiz: ")

    # Kullanıcı çıkmak istediğinde döngüyü sonlandırıyorum
    if secim.lower() == 'q':
        print("\nProgramdan çıkılıyor...")
        break
    
    # Geçersiz seçim kontrol ediyorum
    if secim not in ['1', '2', '3', '4']:
        print("\nGeçersiz işlem. Lütfen 1-4 arasında bir değer giriniz veya çıkmak için 'q' tuşlayınız.")
        continue

    try:
        # Kullanıcıdan sayısal girişler alıyorum
        sayi1 = float(input("\nBirinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
    except ValueError:
        # Hatalı giriş durumu: Kullanıcıya hata mesajı gösteriyorum ve döngüye başa dönüyorum
        print("\nGeçersiz giriş. Lütfen sayısal bir değer giriniz.")
        continue

    # İşlem seçimine göre ilgili fonksiyonu çağırıp sonucu ekrana yazdırıyorum
    if secim == '1':
        print(f"\nGirilen sayıların toplamı: {topla(sayi1, sayi2)}")
    elif secim == '2':
        print(f"\nGirilen sayıların farkı: {cikar(sayi1, sayi2)}")
    elif secim == '3':
        print(f"\nGirilen sayıların çarpımı: {carp(sayi1, sayi2)}")
    elif secim == '4':
        # Bölme işlemi için özel bir kontrol yapıyorum
        bol_sonuc = bol(sayi1, sayi2)
        # Girdi sonuç 0 değilse sonucu yazdırıyorum
        if bol_sonuc is not None:
            print(f"\nSayıların bölümü: {bol_sonuc}")

# Kullanıcı programdan çıktığında bu mesajı gösteriyorum
print("\nProgramdan çıkıldı.")
