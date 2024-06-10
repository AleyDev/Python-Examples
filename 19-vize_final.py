"""
    Girilen vize ve final notu üzerinden vizenin 40 finalin 60 ı alınarak yıl sonu notunu hesaplayan algoritma
"""


# Kullanıcıdan vize notunu al
vize = int(input("Vize notu: "))

# Kullanıcıdan final notunu al
final = int(input("Final notu: "))

# alınan vize notunun %40 ını al ve bir değişkene ata.
a = vize * 0.4
# alınan final notunun %60 ını al ve bir değişkene ata.
b = final * 0.6

# hesaplamalarının toplamını yil sonu notu değişkenine ata
y_sonu = a+b
# yil sonu puanını ekrana yazdır
print("Yıl sonu notunuz: ", y_sonu)