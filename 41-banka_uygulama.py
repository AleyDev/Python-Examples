"""
    BankaHesabi isminde bir sınıf tanımlayınız.
    Üretilen bir nesne:
        "hesapSahibi" isminde bir özelliğe sahip olmalıdır
        "bakiye" isminde bir özelliğe sahip olup, başlangıçta 0.0 değerinde olmalıdır. BankaHesabi("Aleyna K U")
        "paraYatir" metodu oluşturun ve dışaırdan yatırılacak miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarını geri döndürün
        "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün

    hesap = BankaHesabi("Aleyna K U")
    hesap.hesapSahibi => Aleyna K U
    hesap.bakiye => 0.0
    hesap.paraYatir(100000000000000) => 100000000000000.0
    hesap.paraCek(1000000) => 1000000.0

"""



# BankaHesabi isminde bir sınıf tanımlıyorum
class BankaHesabi:
    # __init__ metodu, sınıftan bir nesne oluşturulduğunda çalışır
    # hesapSahibi parametresini alır ve başlangıç bakiyesini 0.0 olarak ayarlar
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi  # hesapSahibi özelliğini ayarlar
        self.bakiye = 0.0  # bakiye özelliğini 0.0 olarak başlatır

    # bakiye değerini döndüren bir metod tanımlıyorum
    def get_bakiye(self):
        return self.bakiye  # mevcut bakiyeyi döndürür

    # para yatırma işlemi için bir metod tanımlıyorum
    def paraYatir(self, miktar):
        self.bakiye += miktar  # verilen miktarı bakiyeye ekler
        return self.bakiye  # güncellenmiş bakiyeyi döndürür
    
    # para çekme işlemi için bir metod tanımlıyorum
    def paraCek(self, miktar):
        # eğer çekilecek miktar bakiyeden büyükse, yetersiz bakiye mesajı verir
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")  # yetersiz bakiye mesajı
            return self.bakiye  # mevcut bakiyeyi döndürür
        else:
            self.bakiye -= miktar  # verilen miktarı bakiyeden çıkarır
            return self.bakiye  # güncellenmiş bakiyeyi döndürür

# BankaHesabi sınıfından bir nesne oluşturuyorum
hesap = BankaHesabi("Aleyna K U")

# Hesap sahibini ve başlangıç bakiyesini kontrol ediyorum
print(hesap.hesapSahibi)  # Aleyna K U yazdırır
print(hesap.get_bakiye())  # 0.0 yazdırır

# Para yatırma işlemi yapıyorum ve sonucu yazdırıyorum
print(hesap.paraYatir(100000000000000))  # 100000000000000.0 yazdırır

# Para çekme işlemi yapıyorum ve sonucu yazdırıyorum
print(hesap.paraCek(1000000))  # 99999000000000.0 yazdırır

# Tekrar bakiye kontrolü yapıyorum ve sonucu yazdırıyorum
print(hesap.get_bakiye())  # 99999000000000.0 yazdırır
