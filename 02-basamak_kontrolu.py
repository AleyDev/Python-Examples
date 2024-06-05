""" 
    Kullanıcıdan 3 basamaklı sayı al, bu sayının basamak değerini ekrana yazdır.
"""


while True:  # Bu döngü kullanıcı doğru bir giriş yapana kadar devam eder.
    # Kullanıcıdan bir giriş alıyoruz
    sayi = input("Lütfen 3 basamaklı bir sayı giriniz: ")

    # Girilen değerin bir sayı olup olmadığını ve 3 basamaklı olup olmadığını kontrol ediyoruz
    if sayi.isdigit() and 100 <= int(sayi) <= 999:  
        # Eğer koşul doğruysa, girilen değeri tam sayıya çeviriyoruz
        sayi = int(sayi)
        
        # Yüzler basamağını hesaplıyoruz. Örneğin, 345 sayısı için 3.
        yuzler_basamagi = sayi // 100
        print("Yüzler basamağındaki sayının basamak değeri: ", yuzler_basamagi)
        
        # Onlar basamağını hesaplıyoruz. Örneğin, 345 sayısı için 4.
        onlar_basamagi = (sayi % 100) // 10
        print("Onlar basamağındaki sayının basamak değeri: ", onlar_basamagi)

        # Birler basamağını hesaplıyoruz. Örneğin, 345 sayısı için 5.
        birler_basamagi = sayi % 10
        print("Birler basamağındaki sayının basamak değeri: ", birler_basamagi)
        
        # Doğru giriş yapıldığında döngüyü sonlandırıyoruz
        break
    else:
        # Eğer koşul yanlışsa, kullanıcıya hata mesajı verip tekrar giriş yapmasını istiyoruz
        print("Hatalı giriş! Lütfen 3 basamaklı bir sayı giriniz.")
