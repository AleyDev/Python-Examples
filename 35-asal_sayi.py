'''
    Soru: Girilen bir sayının asal olup olmadığını bulun.
    ** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

'''

sayi = int(input('Sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False
    
for i in range(2,sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print('Sayı asaldır.')
else:
    print('Asal değildir.')