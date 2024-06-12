"""
    Palindrom: Kelimenin tersinin de kendine eşit olması anlamına gelir.
"""


# Kullanıcıdan bir kelime girmesini isteyin
kelime = input("Bir kelime giriniz: ")

# Kelimenin tersini ekrana yazdırın
print(kelime, 'nin tersi', kelime[::-1], 'dir.')

# Kelimenin palindrom olup olmadığını kontrol edin
if kelime == kelime[::-1]:
    print("Girilen kelime bir palindromdur.")
else:
    print("Girilen kelime bir palindrom değildir.")
