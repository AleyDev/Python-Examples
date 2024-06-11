"""
    İç içe döngüler ile çarpım tablosu oluştur.
"""



# A değişkeni 1'den 10'a kadar (11 dahil değil) döner
for A in range(1, 11):
    # B değişkeni 1'den 10'a kadar (11 dahil değil) döner
    for B in range(1, 11):
        print(A, "*", B, "=", A * B) # A ve B'nin çarpımını ekrana yazdır
    print("\n") # Her A değeri için çarpım tablosunu tamamladıktan sonra bir satır boşluk ekle

