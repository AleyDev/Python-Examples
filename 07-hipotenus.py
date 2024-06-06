"""
    Bir üçgenin hipotenüs uzunluğu
"""


import math  # math kütüphanesini dahil et 

# Kullanıcıdan iki kenar uzunluğu al
a = int(input("Kenar 1 uzunluğu: "))
b = int(input("Kenar 2 uzunluğu: "))

# Hipotenüs uzunluğunu hesapla
c = math.sqrt(a**2 + b**2)  # math kütüphanesinden karekök alma işlemi

# Hesaplanan hipotenüs uzunluğunu ekrana yazdır
print("Hipotenüs uzunluğu: ", c)




"""  # -kütüphane dahil etmeden yazmak istersek-

    # Kullanıcıdan kenar uzunluklarını al
    a = int(input("Kenar 1 uzunluğu: "))
    b = int(input("Kenar 2 uzunluğu: "))

    # Hipotenüs uzunluğunu hesapla
    hipotenus = ((a**2) + (b**2)) ** 0.5

    # Hesaplanan hipotenüs uzunluğunu ekrana yazdır
    print("Hipotenüs uzunluğu: ", hipotenus)

"""