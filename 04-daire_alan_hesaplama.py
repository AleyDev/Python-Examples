"""
    Dairenin alanını hesapla
"""


# π değeri 3,14.. ama sınavlarda tam sayı kısmı alındığını varsayarak 3 olarak tanımlıyorum

pi = 3 
yaricap = int(input("Dairenin yarıçapını giriniz: "))

# Daire alanı formülü >> Daire: alan = π * r ** 2

alan = pi * yaricap ** 2
print(f"Dairenin alanı: {alan:}")