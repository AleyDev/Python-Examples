"""
    Bankamatik Uygulaması:

    Hesap bilgiler tutulacak (dict)
    Menü, Para çekme, Bakiye sorgulama, Para yatırma fonksiyonları tanımlanacak.
    Çekilmek istenen tutar hesapta yoksa, ek hesabın kullanılmak istendiği sorulacak.

"""



# Hesap bilgileri tutulacak (dict)
hesaplar = [
    {
        "ad": "Aley Kaya",
        "hesapNo": "345900",
        "bakiye": 5000000,
        "ekHesap": 10000000,
        "username": "alkaya",
        "password": "1234"
    },
    {
        "ad": "Tu Ug",
        "hesapNo": "593400",
        "bakiye": 1000,
        "ekHesap": 10000000,
        "username": "tu_ug",
        "password": "9876"
    }
]


def menu(hesap):
    """
    Kullanıcı için menü fonksiyonu.
    Bu fonksiyon kullanıcıya yapabileceği işlemleri gösterir ve seçilen işleme göre ilgili fonksiyonu çağırır.
    """
    print("\n" + "-"*30)
    print(f"Merhaba, {hesap['ad']}")
    print("1- Bakiye Sorgula")
    print("2- Para Çekme")
    print("3- Para Yatırma")
    print("4- Çıkış")
    print("-"*30)

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem == "4":
        print("Çıkış yapılıyor...")
        return
    else:
        print("Yanlış seçim!!")

    menu(hesap)


def bakiyeSorgula(hesap):
    """
    Kullanıcının mevcut bakiyesini ve ek hesabını gösterir.
    """
    print(f"Bakiye: {hesap['bakiye']}")
    print(f"Ek Bakiye: {hesap['ekHesap']}")


def paraCekme(hesap):
    """
    Kullanıcının hesaptan para çekmesini sağlar.
    Hesapta yeterli bakiye yoksa ek hesap kullanımı için izin sorar.
    """
    miktar = float(input("Çekmek istediğiniz miktar: "))
    
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzni = input("Ek hesap kullanılsın mı? (E/H): ")

            if ekHesapKullanimIzni.lower() == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print("Üzgünüz, bakiye yetersiz.")
        else:
            print("İzniniz olmadığı için / hesabınızda yeterli bakiye olmadığı için ek hesaptan para çekilemedi.")


def paraYatirma(hesap):
    """
    Kullanıcının hesaba para yatırmasını sağlar.
    """
    miktar = float(input("Yatırmak istediğiniz miktar: "))
    hesap["bakiye"] += miktar
    print(f"{miktar} TL yatırıldı. Güncel bakiye: {hesap['bakiye']}")


def login():
    """
    Kullanıcıdan kullanıcı adı ve parola bilgilerini alır ve doğrular.
    Doğrulama başarılı olursa, kullanıcının hesap bilgilerini kullanarak menüye yönlendirir.
    """
    username = input("Kullanıcı adı: ")
    password = input("Parola: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not isLoggedIn:
        print("Kullanıcı adı ya da parola yanlış")


# Uygulamanın başlangıç noktası
login()
