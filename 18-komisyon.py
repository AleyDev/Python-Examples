"""
    Bir komisyoncu sattığı mallardan fiyatı 50 tlye kadar olanlardan %3, daha fazla olanlardan %2 komisyon almaktadır. Klavyeden girilen 5 malın komisyonlarını bularak toplam komisyonu hesapla.
"""


toplam_komisyon = 0  # Toplam komisyonu tutacak değişkeni tanımla

for _ in range(5):
    fiyat = int(input("Fiyatı girin: "))
    if fiyat <= 50:
        komisyon = fiyat * 0.03
    else:
        komisyon = fiyat * 0.02
    toplam_komisyon += komisyon  # Toplam komisyona kısa bir şekilde komisyon değerini ekle

print("Toplam komisyon: ", toplam_komisyon)
