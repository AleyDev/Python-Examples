import tkinter as tk

# Tkinter uygulamasını başlatıyorum
root = tk.Tk()
root.title("Mesaj Gösterme")
root.minsize(500,250)

# Başlangıçta boş olacak şekilde etiketi oluşturuyorum
label = tk.Label(root, text="", font=('Arial', 24))
label.pack(pady=20)

# Tuşa basıldığında mesajı gösteren fonksiyonu tanımlıyorum
def show_message():
    label.config(text="Merhaba, Tkinter!")

# Tuşu oluşturuyorum ve ekrana yerleştiriyorum
button = tk.Button(root, text="Mesajı Göster", command=show_message, font=('Arial', 18))
button.pack(pady=20)

# Uygulamayı çalıştırıyorum
root.mainloop()
