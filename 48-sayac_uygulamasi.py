import tkinter as tk  # Tkinter kütüphanesini içe aktarıyorum.

# Ana pencereyi oluşturuyorum ve başlık ile boyutunu ayarlıyorum
root = tk.Tk()
root.title("Sayacı Başlat/Durdur Uygulaması")
root.geometry("300x200")

# Sayaç başlangıç değerini sıfır olarak belirliyorum
counter = 0

# Sayaç durumu için bir bayrak (flag) oluşturuyorum, başlangıçta sayaç çalışmıyor (False)
is_running = False

# Sayaç değerini ekranda göstermek için bir etiket (label) oluşturuyorum
label = tk.Label(root, text="0", font=('Arial', 48))
label.pack(pady=20)  # Etiketi yerleştiriyorum, biraz yukarıdan boşluk bırakıyorum (pady)

# Sayaç değerini her saniye artıran ve etiketi güncelleyen fonksiyon
def update_counter():
    if is_running:  # Eğer sayaç çalışıyorsa
        global counter  # Sayaç değerini global olarak tanımlıyorum
        counter += 1  # Sayaç değerini 1 artırıyorum
        label.config(text=str(counter))  # Etiketi güncelleyerek yeni sayaç değerini gösteriyorum
        root.after(1000, update_counter)  # 1 saniye sonra bu fonksiyonu tekrar çalıştırıyorum

# Sayaç çalışmaya başladığında çalışan fonksiyon
def start_counter():
    global is_running  # Sayaç durumu bayrağını global olarak tanımlıyorum
    is_running = True  # Sayaç çalışmaya başlıyor
    update_counter()  # Sayaç güncelleme fonksiyonunu çağırıyorum

# Sayaç durdurulduğunda çalışan fonksiyon
def stop_counter():
    global is_running  # Sayaç durumu bayrağını global olarak tanımlıyorum
    is_running = False  # Sayaç duruyor

# Sayaç sıfırlama işlemi yapan fonksiyon
def reset_counter():
    global counter  # Sayaç değerini global olarak tanımlıyorum
    counter = 0  # Sayaç değerini sıfırlıyorum
    label.config(text="0")  # Etiketi güncelleyerek sıfır değerini gösteriyorum
    stop_counter()  # Sayaç durdurma fonksiyonunu çağırıyorum

# Sayaç başlatma düğmesini oluşturuyorum ve sol tarafa yerleştiriyorum
start_button = tk.Button(root, text="Başlat", command=start_counter, font=('Arial', 18))
start_button.pack(side='left', padx=20, pady=20)  # Düğmeyi biraz boşluk bırakarak yerleştiriyorum

# Sayaç durdurma düğmesini oluşturuyorum ve sağ tarafa yerleştiriyorum
stop_button = tk.Button(root, text="Durdur", command=stop_counter, font=('Arial', 18))
stop_button.pack(side='right', padx=20, pady=20)  # Düğmeyi biraz boşluk bırakarak yerleştiriyorum

# Sayaç sıfırlama düğmesini oluşturuyorum ve alt tarafa yerleştiriyorum
reset_button = tk.Button(root, text="Sıfırla", command=reset_counter, font=('Arial', 18))
reset_button.pack(pady=20)  # Düğmeyi biraz boşluk bırakarak yerleştiriyorum

# Ana döngüyü başlatıyorum, böylece GUI açık kalıyor ve kullanıcı girişlerini bekliyor
root.mainloop()
