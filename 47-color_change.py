"""
    Bu uygulama, bir düğmeye basarak pencerenin arka plan rengini değiştiren basit bir uygulamadır.
"""

import tkinter as tk
import random

# Uygulamayı başlatıyorum
root = tk.Tk()
root.title("Renk Değiştirme Uygulaması")
root.geometry("300x200")

# Arka plan rengini rastgele bir renkle değiştiren fonksiyonu tanımlıyorum
def change_color():
    colors = ["red", "dark green", "blue", "yellow", "purple", "orange", "pink", "black", "brown", "white", "grey"]
    random_color = random.choice(colors)
    root.configure(bg=random_color)

# Düğmeyi oluşturuyorum ve pencereye yerleştiriyorum
button = tk.Button(root, text="Rengi Değiştir", command=change_color, font=('Arial', 18))
button.pack(expand=True)

# Uygulamayı çalıştırıyorum
root.mainloop()
