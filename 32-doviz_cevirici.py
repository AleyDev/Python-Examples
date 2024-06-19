"""
    Kullanıcıdan alınan bir tutarı belirli bir döviz kuru üzerinden çevirme ve ekrana yazdırma işlemi.
"""


# Döviz çevirici fonksiyonunu tanımlıyorum
def doviz_cevir(tutar, kur):
    # Tutara döviz kurunu uygulayarak çeviri işlemini yapıyorum
    return tutar * kur

# Kullanıcıdan döviz çevirme bilgilerini alıyorum
# Kullanıcıdan çevirmek istediği tutarı girmesini istiyorum
tutar = float(input("Çevirmek istediğiniz tutarı girin: "))
# Kullanıcıdan döviz kurunu girmesini istiyorum
kur = float(input("Döviz kurunu girin: "))

# Döviz çevirici fonksiyonunu çağırarak sonucu ekrana yazdırıyorum
# Kullanıcının girdiği tutar ve kur ile doviz_cevir fonksiyonunu çağırarak sonucu değişkene atıyorum
sonuc = doviz_cevir(tutar, kur)
# Çeviri sonucunu ekrana yazdırıyorum
print(f"Çevrilen tutar: {sonuc}")
