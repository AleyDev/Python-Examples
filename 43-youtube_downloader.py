"""                     1                    """



import pytube  # YouTube videolarını indirmek için PyTube kütüphanesini içe aktarıyorum.

url = input("enter video url: ")  # Kullanıcıdan indirmek istediği YouTube videosunun URL'sini girmesini istiyorum.

path = ""  # İndirilecek dosyanın kaydedileceği yolu belirliyorum. Boş bırakıldığında varsayılan olarak geçerli dizine indirir.

# YouTube nesnesi oluşturuyorum ve en yüksek çözünürlüklü akışı bulup belirtilen yola indiriyorum.
pytube.YouTube(url).streams.get_highest_resolution().download(path)




"""                     2                    """


# YouTube Downloader script'i pytube kütüphanesini kullanarak video indirmek için

# Gerekli kütüphaneyi içe aktarıyorum
from pytube import YouTube

# YouTube videosunu indirmek için bir fonksiyon tanımlıyorum
def video_indir(url):
    """
    Verilen URL'den bir YouTube videosunu indirir.
    
    Parametreler:
    url (str): İndirilecek YouTube videosunun URL'si.
    """
    # Sağlanan URL ile bir YouTube nesnesi oluşturuyorum
    yt = YouTube(url)
    
    # Mevcut en yüksek çözünürlüklü akışı alıyorum
    stream = yt.streams.get_highest_resolution()
    
    # Videoyu indirme işlemini başlatıyorum
    stream.download()
    print(f"İndirildi: {yt.title}")  # İndirme işlemi tamamlandığında kullanıcıya video başlığı ile birlikte bilgi veriyorum

# Ana kod bloğu
if __name__ == "__main__":
    # Kullanıcıdan YouTube video URL'sini girmesini istiyorum
    video_url = input("YouTube video URL'sini girin: ")
    
    # Sağlanan URL ile indirme fonksiyonunu çağırıyorum
    video_indir(video_url)



"""                     3                    """


import pytube  # YouTube videolarını indirmek için PyTube kütüphanesini içe aktarıyorum.
import os  # Dosya ve dizin işlemleri için os modülünü içe aktarıyorum.

def download_youtube_video():
    try:
        url = input("İndirmek istediğiniz YouTube videosunun URL'sini girin: ")  # Kullanıcıdan YouTube URL'sini alıyorum.
        
        # İndirilecek dosyanın kaydedileceği yolu kullanıcıdan alıyorum. Varsayılan olarak geçerli dizini kullanıyorum.
        path = input("Videoyu kaydetmek istediğiniz dizini girin (varsayılan: geçerli dizin): ").strip()
        if not path:  # Kullanıcı bir yol girmezse
            path = os.getcwd()  # Geçerli çalışma dizinini kullanıyorum.
        
        print("Video indiriliyor... Lütfen bekleyin.")
        pytube.YouTube(url).streams.get_highest_resolution().download(path)  # Videoyu en yüksek çözünürlükte indiriyorum.
        
        print(f"Video başarıyla indirildi ve {path} dizinine kaydedildi.")  # Başarılı indirme mesajı.
    except pytube.exceptions.PytubeError as e:  # PyTube ile ilgili olası hataları yakalıyorum.
        print(f"Bir hata oluştu: {e}")
    except Exception as e:  # Diğer olası hataları yakalıyorum.
        print(f"Beklenmeyen bir hata oluştu: {e}")

# YouTube videosunu indirmek için fonksiyonu çağırıyorum.
download_youtube_video()
