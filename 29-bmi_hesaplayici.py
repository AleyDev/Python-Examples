"""
Kullanıcıdan alınan boy ve kilo değerlerine göre Vücut Kitle İndeksini (VKİ) hesaplama ve kategorilendirme işlemi
"""

# BMI hesaplama fonksiyonunu tanımlıyorum
def bmi_hesaplama(boy, kilo):
    # Boyu metre cinsine çeviriyorum
    boy_metre = boy / 100
    # BMI değerini hesaplıyorum ve virgülden sonra iki basamak olacak şekilde yuvarlıyorum
    v_k_indeksi = round(kilo / (boy_metre ** 2), 2)
    # Kullanıcıya BMI değerini yazdırıyorum
    print(f"Vücut kitle indeksiniz: {v_k_indeksi}")

    # BMI değerine göre kategoriyi belirliyorum ve kullanıcıya durumu yazdırıyorum
    if v_k_indeksi <= 18.5:
        print("Durumunuz: Zayıf")
    elif 18.5 < v_k_indeksi < 24.9:
        print("Durumunuz: Normal")
    elif 25 < v_k_indeksi < 29.9:
        print("Durumunuz: Kilolu")
    elif 30 < v_k_indeksi < 34.9:
        print("Durumunuz: 1. derece obezite - (Fazla kilolu)")
    elif 35 < v_k_indeksi < 39.9:
        print("Durumunuz: 2. derece obezite - (Obez)")
    elif v_k_indeksi >= 40:
        print("Durumunuz: 3. derece obezite - (Aşırı obez)")

# Kullanıcıdan boy ve kilo bilgilerini alıyorum
boy = float(input("Boyunuzu (cm cinsinden) giriniz: "))
kilo = float(input("Kilonuzu (kg cinsinden) giriniz: "))

# BMI hesaplama fonksiyonunu çalıştırıyorum
bmi_hesaplama(boy, kilo)

