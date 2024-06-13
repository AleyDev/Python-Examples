"""
    Hasta muayene sıra yönetim sistemi
"""

# Boş bir liste oluşturuyorum. Bu liste hastaların TC kimlik numaralarını saklayacak.
liste = []

# Sonsuz döngü başlatıyorum. Bu döngü kullanıcının sürekli işlem yapabilmesi için.
while True:
    # Kullanıcıya menü gösteriyorum.
    print("\nMenü:")
    print("1. TC numarası ile muayene sırası kontrolü")
    print("2. Doktora gitmesi gereken hastayı çağır")
    print("3. Yeni hasta ekle")
    print("4. Çıkış")
    
    # Kullanıcıdan menüdeki seçeneklerden birini girmesini istiyorum.
    secim = int(input("Seçiminizi yapınız (1-4): "))

    # Kullanıcı 1. seçeneği seçerse, muayene sırasını kontrol edeceğiz.
    if secim == 1:
        # Kullanıcıdan TC numarasını girmesini istiyorum.
        tc = int(input("TC numaranızı giriniz: "))
        # Girilen TC numarası listede varsa...
        if tc in liste:
            # TC numarasının listedeki sırasını buluyorum.
            i = liste.index(tc)
            # Sırasını ekrana yazdırıyorum. İndeks 0'dan başladığı için 1 ekliyorum.
            print(f"{tc} TC numaralı hastanın muayene sırası: {i+1}")
        else:
            # TC numarası listede yoksa, uyarı mesajı gösteriyorum.
            print(f"{tc} TC numaralı hasta bulunamadı.")

    # Kullanıcı 2. seçeneği seçerse, sıradaki hastayı doktora çağıracağız.
    elif secim == 2:
        # Listede bekleyen hasta varsa...
        if len(liste) > 0:
            # İlk sıradaki hastayı (listenin başındaki) doktora çağırıyorum.
            print(f"{liste[0]} TC numaralı hasta, doktorun yanına gidiniz.")
            # Çağrılan hastayı listeden çıkarıyorum.
            liste.pop(0)
        else:
            # Listede bekleyen hasta yoksa, uyarı mesajı gösteriyorum.
            print("Bekleyen hasta yok.")

    # Kullanıcı 3. seçeneği seçerse, yeni bir hasta ekleyeceğiz.
    elif secim == 3:
        # Kullanıcıdan TC numarasını girmesini istiyorum.
        tc = int(input("TC numaranızı giriniz: "))
        # Girilen TC numarası zaten listede varsa...
        if tc in liste:
            # Uyarı mesajı gösteriyorum.
            print(f"{tc} TC numaralı hasta zaten listede.")
        else:
            # TC numarası listede yoksa, listeye ekliyorum.
            liste.append(tc)
            # Ekleme işlemini onaylayan mesaj gösteriyorum.
            print(f"{tc} TC numaralı hasta listeye alındı.")

    # Kullanıcı 4. seçeneği seçerse, programdan çıkacağız.
    elif secim == 4:
        # Çıkış mesajı gösteriyorum.
        print("Çıkış yapılıyor...")
        # Sonsuz döngüyü kırarak programı sonlandırıyorum.
        break

    # Kullanıcı geçersiz bir seçim yaparsa...
    else:
        # Uyarı mesajı gösteriyorum.
        print("Geçersiz seçim. Lütfen 1-4 arasında bir seçenek giriniz.")


# Bu sistem, hastaların muayene sırasını etkili bir şekilde yönetmeyi sağlar