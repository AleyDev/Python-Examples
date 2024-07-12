# Öncelikle, veriyi bir dosyaya kaydetmek için bir fonksiyon tanımlıyorum.
def veri_kaydetme(dosya_adi, veri):
    # 'with' ifadesi, dosya işlemlerini güvenli bir şekilde yapmamı sağlar. Dosyayı 'a' (append) modunda açıyorum.
    with open(dosya_adi, 'a') as dosya:
        # Dosyaya veri ekliyorum ve her veri girişinden sonra yeni bir satıra geçiyorum.
        dosya.write(veri + '\n')



# Ardından, dosyadan veri okumak için bir fonksiyon tanımlıyorum.
def veri_okuma(dosya_adi):
    # 'with' ifadesi ile dosyayı 'r' (read) modunda açıyorum.
    with open(dosya_adi, 'r') as dosya:
        # Dosyadaki tüm satırları okuyorum ve liste olarak saklıyorum.
        veriler = dosya.readlines()
        # Her satırdaki boşlukları kaldırarak yeni bir liste oluşturuyorum ve bu listeyi döndürüyorum.
        return [veri.strip() for veri in veriler]



# Şimdi, ana işlevi tanımlıyorum. Bu işlev kullanıcı ile etkileşime geçiyor ve veri kaydetme/okuma işlemlerini yönetiyor.
def main():
    # Kullanacağım dosya adını belirliyorum.
    dosya_adi = 'veriler.txt'
    while True:
        # Kullanıcıdan yapmak istediği işlemi seçmesini istiyorum.
        secim = input("Veri kaydetmek için '1', verileri okumak için '2', çıkmak için 'q' girin: ")

        if secim == '1':
            # Kullanıcı veri kaydetmeyi seçerse, kaydedilecek veriyi alıyorum.
            veri = input("Kaydedilecek veriyi girin: ")
            # Veriyi dosyaya kaydediyorum.
            veri_kaydetme(dosya_adi, veri)
            print("Veri başarıyla kaydedildi.")
        elif secim == '2':
            # Kullanıcı verileri okumayı seçerse, dosyadan verileri okuyorum.
            veriler = veri_okuma(dosya_adi)
            if veriler:
                # Eğer dosyada veri varsa, verileri ekranda gösteriyorum.
                print("Kaydedilen veriler:")
                for veri in veriler:
                    print(veri)
            else:
                # Eğer dosyada veri yoksa, kullanıcıya bilgi veriyorum.
                print("Henüz kaydedilmiş veri yok.")
        elif secim == 'q':
            # Kullanıcı çıkmayı seçerse, programdan çıkıyorum.
            print("Programdan çıkılıyor.")
            break
        else:
            # Geçersiz bir seçim yapılırsa, kullanıcıyı uyarıyorum.
            print("Geçersiz seçim, lütfen tekrar deneyin.")


# Bu dosya doğrudan çalıştırıldığında ana işlevi çağırıyorum.
if __name__ == "__main__":
    main()
