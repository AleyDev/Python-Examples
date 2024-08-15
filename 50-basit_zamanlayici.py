
import tkinter as tk
from tkinter import messagebox
import winsound  # Windows'ta ses çalmak için kullanıyorum

# Ana pencereyi oluşturuyorum
root = tk.Tk()
root.title("TUA Basit Zamanlayıcı")
root.geometry("300x150")

# Kullanıcıdan süreyi girmesini isteyeceğim etiket ve giriş alanı oluşturuyorum
tk.Label(root, text="Süreyi saniye olarak girin:").pack(pady=10)
time_entry = tk.Entry(root, width=10)
time_entry.pack(pady=5)

def start_timer():
    """Zamanlayıcıyı başlatıyorum."""
    try:
        # Kullanıcının girdiği süreyi alıyorum
        countdown_time = int(time_entry.get())
        if countdown_time > 0:
            countdown(countdown_time)
        else:
            messagebox.showerror("Hata", "Lütfen pozitif bir sayı girin.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

def countdown(time_left):
    """Geri sayımı başlatıyorum ve zamanı ekranda gösteriyorum."""
    if time_left > 0:
        time_entry.delete(0, tk.END)  # Giriş alanını temizliyorum
        time_entry.insert(0, str(time_left))  # Kalan süreyi giriş alanında gösteriyorum
        root.after(1000, countdown, time_left - 1)  # 1 saniye sonra tekrar çağırıyorum
    else:
        show_notification()

def show_notification():
    """Zaman dolduğunda bildirim penceresini gösteriyorum ve ses çalıyorum."""
    winsound.Beep(1000, 1000)  # 1000 Hz frekansında 1 saniye süren bir bip sesi çalıyorum
    messagebox.showinfo("Zamanlayıcı", "Süre doldu!")  # Bildirim olarak basit bir bilgi penceresi açıyorum

# "Başlat" düğmesini oluşturuyorum
start_button = tk.Button(root, text="Başlat", command=start_timer)
start_button.pack(pady=20)

# Ana döngüyü başlatıyorum
root.mainloop()
