"""
    Kullanıcıdan cevap alarak soruları yanıtlamasını sağlayan ve doğru cevapları sayarak skor tutan basit bir quiz uygulaması oluşturur.
"""

# Soru sınıfını tanımlıyorum
class Question:
    def __init__(self, text, choices, answer):
        # Soru sınıfının kurucusu, soru metnini, seçenekleri ve doğru cevabı alır.
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        # Kullanıcının cevabının doğru olup olmadığını kontrol eder.
        return self.answer == answer

# Quiz sınıfını tanımlıyorum
class Quiz:
    def __init__(self, questions):
        # Quiz sınıfının kurucusu, sorular listesini, skoru ve soru indeksini başlatır.
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        # Geçerli soruyu döndürür.
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        # Geçerli soruyu ve seçeneklerini görüntüler, kullanıcıdan cevap alır ve `guess` metodunu çağırır.
        question = self.getQuestion()  # Geçerli soruyu alır.
        print(f"Soru {self.questionIndex + 1}: {question.text}")  # Soruyu yazdırır.

        for q in question.choices:  # Seçenekleri yazdırır.
            print('- ' + q)
        answer = input("Cevabınızı girin: ")  # Kullanıcıdan cevap alır.
        
        self.guess(answer)  # Cevabı kontrol eder.
        self.loadQuestion()  # Bir sonraki soruyu yükler.

    def guess(self, answer):
        # Kullanıcının cevabını kontrol eder, doğruysa skoru artırır, her durumda bir sonraki soruya geçer.
        question = self.getQuestion()  # Geçerli soruyu alır.

        if question.checkAnswer(answer):  # Cevabın doğruluğunu kontrol eder.
            self.score += 1  # Doğruysa skoru artırır.
        self.questionIndex += 1  # Bir sonraki soruya geçer.

    def loadQuestion(self):
        # Soruları yükler ve quizin bitip bitmediğini kontrol eder.
        if len(self.questions) == self.questionIndex:  # Tüm sorular sorulduysa
            self.showScore()  # Skoru gösterir.
        else:
            self.displayQuestion()  # Bir sonraki soruyu görüntüler.
    
    def showScore(self):
        # Quiz bittiğinde kullanıcıya skoru gösterir.
        print(f"Quiz bitti! Skorunuz: {self.score}/{len(self.questions)}")  # Skoru yazdırır.

# Soruları tanımlıyorum
q1 = Question("En iyi programlama dili hangisidir?", ["C#", "Python", "Javascript", "Java"], "Python")
q2 = Question("En popüler programlama dili hangisidir?", ["C#", "Javascript", "Python", "Java"], "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["Java", "C#", "Python", "Javascript"], "Python")
questions = [q1, q2, q3]  # Sorular listesini oluşturuyorum.

# Quiz'i başlatıyorum
quiz = Quiz(questions)  # Quiz nesnesini oluşturuyorum.
quiz.loadQuestion()  # Soruları yüklemeye başlıyorum.
