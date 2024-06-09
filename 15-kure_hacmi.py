"""
    Kürenin hacmini hesapla.
    Kürenin hacmi: 4/3*pi*r**3
"""


import math  # math kütüphanesini dahil et

yaricap = float(input("Yarıçap: "))  # Kullanıcıdan yarıçapı al

# Kürenin hacmini hesapla
hacim = (4/3) * math.pi * yaricap**3

# Hesaplanan hacmi ekrana yazdır
print("Kürenin hacmi: ", hacim)
