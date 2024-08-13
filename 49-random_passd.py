import tkinter as tk
import random
import string

# Ana pencereyi oluşturuyorum
root = tk.Tk()
root.title("TUA Random Şifre Oluşturucu")
root.geometry("400x200")

# Şifre uzunluğunu girmek için etiket ve giriş alanı oluşturuyorum
tk.Label(root, text="Şifre Uzunluğu:").pack(pady=10)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

def generate_password():
    """Rastgele bir şifre oluşturuyorum."""
    length = int(length_entry.get())  # Kullanıcının girdiği şifre uzunluğunu alıyorum
    # Rastgele şifre oluşturuyorum
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Oluşturulan Şifre: {password}")  # Oluşan şifreyi ekranda gösteriyorum

# "Şifre Oluştur" düğmesini oluşturuyorum
generate_button = tk.Button(root, text="Şifre Oluştur", command=generate_password)
generate_button.pack(pady=20)

# Oluşan şifreyi göstermek için etiket oluşturuyorum
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Ana döngüyü başlatıyorum
root.mainloop()
