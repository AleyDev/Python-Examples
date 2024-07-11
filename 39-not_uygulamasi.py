"""
    Not Uygulaması

    Menu
        -Not Gir
        -Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
        -Notları Kayıt Et
        -Çıkış
"""

def notGir():
    try:
        # Öğrenci adını alıyorum
        ad = input("Öğrenci adı: ")
        # Öğrenci soyadını alıyorum
        soyad = input("Öğrenci soyadı: ")
        # Vize notunu alıyorum ve tamsayıya çeviriyorum
        vize = int(input("Vize Notunuz: "))
        # Final notunu alıyorum ve tamsayıya çeviriyorum
        final = int(input("Final Notunuz: "))

        # Vize ve final notlarının 0 ile 100 arasında olup olmadığını kontrol ediyorum
        if not (0 <= vize <= 100 and 0 <= final <= 100):
            raise ValueError("Notlar 0 ile 100 arasında olmalıdır.")
        
        # Notları "sinav_notlari.txt" dosyasına ekleme modunda açıyorum
        with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
            # Öğrenci adını, soyadını ve notlarını dosyaya yazıyorum
            file.write(f"{ad} {soyad}: {vize}, {final}\n")
    
    except ValueError as e:
        # Hata durumunda kullanıcıya bilgi veriyorum
        print(f"Hata: {e}")


def notHesapla(satir):
    # Satırdaki gereksiz boşlukları temizliyorum
    satir = satir.strip()
    # Satırı ":" karakterinden ayırıyorum
    liste = satir.split(":")
    
    # Öğrenci adını ve soyadını alıyorum
    ogrenciAdi = liste[0]
    # Vize ve final notlarını ayırıyorum
    notlar = liste[1].split(",")

    # Vize ve final notlarını tamsayıya çeviriyorum
    vizeNotu = int(notlar[0].strip())
    finalNotu = int(notlar[1].strip())

    # Vize notunun %30'u ve final notunun %70'ini alarak ortalamayı hesaplıyorum
    ortalama = (vizeNotu * 0.3) + (finalNotu * 0.7)
    
    # Ortalama değerine göre harf notunu belirliyorum
    if 90 <= ortalama <= 100:
        harfNotu = "AA"
    elif 85 <= ortalama < 90:
        harfNotu = "BA"
    elif 80 <= ortalama < 85:
        harfNotu = "BB"
    elif 75 <= ortalama < 80:
        harfNotu = "CB"
    elif 70 <= ortalama < 75:
        harfNotu = "CC"
    elif 65 <= ortalama < 70:
        harfNotu = "DC"
    elif 60 <= ortalama < 65:
        harfNotu = "DD"
    elif 55 <= ortalama < 60:
        harfNotu = "FD"
    else:
        harfNotu = "FF"

    # Hesaplanan ortalama ve harf notunu döndürüyorum
    return f"{ogrenciAdi}: Ortalama={ortalama:.2f}, Harf Notu={harfNotu}"


def notlariOku():
    try:
        # "sinav_notlari.txt" dosyasını okuma modunda açıyorum
        with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
            # Dosyadaki her satırı okuyorum
            for satir in file:
                # Hesaplanan notları ekrana yazdırıyorum
                print(notHesapla(satir))
    except FileNotFoundError:
        # Dosya bulunamadığında kullanıcıya bilgi veriyorum
        print("Not dosyası bulunamadı.")


def notlariKaydet():
    try:
        # "sinav_notlari.txt" dosyasını okuma modunda açıyorum
        with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
            # Hesaplanmış sonuçları yazmak için "sonuclar.txt" dosyasını yazma modunda açıyorum
            with open("sonuclar.txt", "w", encoding="utf-8") as output:
                # Dosyadaki her satırı okuyorum
                for satir in file:
                    # Hesaplanmış notları alıyorum
                    hesaplanmis = notHesapla(satir)
                    # Hesaplanmış notları "sonuclar.txt" dosyasına yazıyorum
                    output.write(hesaplanmis + "\n")
        # Kullanıcıya başarı mesajı veriyorum
        print("Notlar başarıyla kaydedildi.")
    except FileNotFoundError:
        # Dosya bulunamadığında kullanıcıya bilgi veriyorum
        print("Not dosyası bulunamadı.")                 


while True:
    # Menü seçeneklerini ekrana yazdırıyorum
    print("Menü:\n1-Not Gir\n2-Notları Oku\n3-Notları Kayıt Et\n4-Çıkış\n")
    
    # Kullanıcıdan yapmak istediği işlemi alıyorum
    islem = input("Lütfen Yapmak İstediğiniz İşlemi Seçin: ")

    if islem == "1":
        # Not girmek için notGir fonksiyonunu çağırıyorum
        notGir()
    elif islem == "2":
        # Notları okumak için notlariOku fonksiyonunu çağırıyorum
        notlariOku()
    elif islem == "3":
        # Notları kaydetmek için notlariKaydet fonksiyonunu çağırıyorum
        notlariKaydet()
    elif islem == "4":
        # Çıkış işlemini gerçekleştiriyorum
        print("Çıkış yapılıyor.")
        break
    else:
        # Geçersiz işlem girişi durumunda uyarı mesajı veriyorum
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
