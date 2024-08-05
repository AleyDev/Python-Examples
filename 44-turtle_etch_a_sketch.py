"""
    Bu proje, ok tuşlarını kullanarak ekranda çizim yapmanıza olanak tanır. "c" tuşu ile çizimi temizleyebilir ve "q" tuşu ile programdan çıkabilirsiniz.
"""

import turtle  # turtle modülünü içe aktarıyorum

# Ekranı oluşturuyorum
screen = turtle.Screen()  # Turtle için bir ekran oluşturuyorum
screen.title("Turtle Etch-A-Sketch")  # Ekran başlığını belirliyorum
screen.bgcolor("white")  # Ekran arka plan rengini beyaz yapıyorum

# Turtle objesi oluşturuyorum
sketch_turtle = turtle.Turtle()  # Çizim yapmak için bir turtle objesi oluşturuyorum
sketch_turtle.shape("turtle")  # Turtle şeklinin görünümünü "kaplumbağa" olarak belirliyorum
sketch_turtle.color("black")  # Turtle rengini siyah yapıyorum
sketch_turtle.speed(1)  # Turtle hareket hızını 1 yapıyorum (yavaş)

# Hareket fonksiyonları
def move_forward():
    sketch_turtle.forward(10)  # Turtle'ı 10 birim ileri hareket ettiriyorum

def move_backward():
    sketch_turtle.backward(10)  # Turtle'ı 10 birim geri hareket ettiriyorum

def turn_left():
    sketch_turtle.left(15)  # Turtle'ı 15 derece sola döndürüyorum

def turn_right():
    sketch_turtle.right(15)  # Turtle'ı 15 derece sağa döndürüyorum

def clear_drawing():
    sketch_turtle.clear()  # Ekrandaki tüm çizimleri temizliyorum

def exit_program():
    screen.bye()  # Programdan çıkıyorum ve ekranı kapatıyorum

# Klavye kontrollerini atıyorum
screen.listen()  # Ekranın klavye girişlerini dinlemesini sağlıyorum
screen.onkey(move_forward, "Up")  # Yukarı ok tuşuna basıldığında move_forward fonksiyonunu çağırıyorum
screen.onkey(move_backward, "Down")  # Aşağı ok tuşuna basıldığında move_backward fonksiyonunu çağırıyorum
screen.onkey(turn_left, "Left")  # Sol ok tuşuna basıldığında turn_left fonksiyonunu çağırıyorum
screen.onkey(turn_right, "Right")  # Sağ ok tuşuna basıldığında turn_right fonksiyonunu çağırıyorum
screen.onkey(clear_drawing, "c")  # "c" tuşuna basıldığında clear_drawing fonksiyonunu çağırıyorum
screen.onkey(exit_program, "q")  # "q" tuşuna basıldığında exit_program fonksiyonunu çağırıyorum

# Ana döngü
screen.mainloop()  # Turtle ekranının kapanmamasını ve sürekli dinlemesini sağlıyorum




"""
    "Etch-A-Sketch" ismi, 1960'larda icat edilen ve oldukça popüler olan mekanik bir çizim oyuncağından gelir. Etch-A-Sketch, iki düğme kullanarak ekranda çizim yapmanıza olanak tanıyan bir cihazdır. Bir düğme yatay hareketi, diğeri ise dikey hareketi kontrol eder. Çizimi temizlemek için cihazı sallamanız yeterlidir.

    "Turtle Etch-A-Sketch" adı, turtle modülünü kullanarak benzer bir çizim deneyimi sunduğu için verilmiştir. Turtle'ın hareketlerini ok tuşlarıyla kontrol ederek ekranda çizim yapıyorsunuz. Ek olarak, "c" tuşu ile çizimi temizleyebiliyor ve "q" tuşu ile programdan çıkabiliyorsunuz.

    Bu isim, kullanıcıya hemen projenin amacını ve nasıl çalıştığını anlatan tanıdık ve açıklayıcı bir isimdir. Böylece, turtle modülü kullanarak etkileşimli bir çizim uygulaması yapıldığını kolayca anlayabiliriz.
    
    Bu proje, öğrenme sürecimde geliştirdiğim basit bir uygulamadır ve geliştirmeye açıktır. Her türlü geri bildirim ve katkıya açık olduğumu belirtmek isterim.
"""