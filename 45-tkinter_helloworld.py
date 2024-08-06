import tkinter as tk

# Tkinter uygulamasını başlatıyorum
root = tk.Tk()
root.title("Hello World")

# Etiketi oluşturuyorum ve pencereye yerleştiriyorum
label = tk.Label(root, text="Hello World!", font=('Arial', 24))
label.pack(pady=20)

# Uygulamayı çalıştırıyorum
root.mainloop()
