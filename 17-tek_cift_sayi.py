"""
    1 - 99 sayıları arasındaki tek ve çift sayıların toplamları ile çarpımlarını ayrı ayrı hesapla.
"""


# başlangıç değerlerini ata
toplam_cift = 0
carpim_cift = 1
toplam_tek = 0
carpim_tek = 1

for i in range(1, 100):
    if i % 2 == 0:
        toplam_cift += i
        carpim_cift *= i
    else:
        toplam_tek += i
        carpim_tek *= i

print("1-99 arasındaki çift sayıların toplamı:", toplam_cift)
print("1-99 arasındaki çift sayıların çarpımı:", carpim_cift)
print("1-99 arasındaki tek sayıların toplamı:", toplam_tek)
print("1-99 arasındaki tek sayıların çarpımı:", carpim_tek)