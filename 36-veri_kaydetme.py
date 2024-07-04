"""
    Kullanıcıdan alınan verileri dosyaya kaydetme işlemi
"""



# Kullanıcıdan veri alıyorum

isim = input("Lütfen isminizi girin: ")  # isim bilgisi alıyorum
yas = input("Lütfen yaşınızı girin: ")   # yaş bilgisi alıyorum


# Dosyaya veri yazma işlemini yapıyorum

dosya_adi = 'kullanici_bilgileri.txt'  # Oluşturup yazılacak dosyayı oluşturuyorum

try:
    dosya = open(dosya_adi, 'a', encoding='utf-8')  # Dosyayı ekleme modunda açıyorum, UTF-8 kodlaması kullanıyorum
    dosya.write(f"İsim: {isim}, Yaş: {yas}\n")  # Kullanıcı bilgilerini dosyaya yazıyorum
    dosya.close()  # Dosyayı kapatıyorum
    print(f"Bilgiler {dosya_adi} dosyasına kaydedildi.")  # Başarı mesajı yazdırıyorum
except IOError:  # Dosya yazma hatası oluşursa bu blok çalışır
    print(f"{dosya_adi} dosyasına yazılırken bir hata oluştu.")  # Hata mesajı yazdırıyorum


"""
Deneme

Lütfen isminizi girin: Aleyna
Lütfen yaşınızı girin: 24

Bilgiler kullanici_bilgileri.txt dosyasına kaydedildi.

Kaydedilen bilgi ---------> İsim: aleyna kaya, Yaş: 24

"""



"""
Kodu try-except ko bloğunda yazmak zorunda değilsiniz.

dosya_adi = 'kullanici_bilgileri.txt'  # Yazacağımız dosyanın adı

# Dosyayı 'a' (append) modunda açıp yazma işlemini gerçekleştiriyoruz
dosya = open(dosya_adi, 'a', encoding='utf-8')
dosya.write(f"İsim: {isim}, Yaş: {yas}\n")
dosya.close()  # İşlem tamamlandıktan sonra dosyayı kapatıyoruz

print(f"Bilgiler {dosya_adi} dosyasına kaydedildi.")
 

Bu şekilde de çalıştırabilirsiniz.

"""