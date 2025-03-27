import random
import time
import turtle

# 1. Simulasi Undian Acak dengan Animasi

def undian_acak():
    peserta = ["Iqbal", "Aqila", "Dani", "Siti", "Budi", "Tina"]
    print("Memulai undian...")
    time.sleep(2)
    pemenang = random.choice(peserta)
    print(f"Selamat kepada {pemenang} yang memenangkan hadiah!")

undian_acak()


# 2. Fraktal Pohon dengan Turtle (Grafis)

def pohon_fraktal(cabang, ukuran):
    if ukuran < 5:
        return
    turtle.forward(ukuran)
    turtle.left(cabang)
    pohon_fraktal(cabang, ukuran - 10)
    turtle.right(cabang * 2)
    pohon_fraktal(cabang, ukuran - 10)
    turtle.left(cabang)
    turtle.backward(ukuran)

# Setup Turtle
screen = turtle.Screen()
turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.color("green")
pohon_fraktal(30, 100)
screen.mainloop()


# 3. Chatbot Sederhana dengan Logika Respon

def chatbot():
    print("Selamat datang di Chatbot! Ketik 'bye' untuk keluar.")
    while True:
        user_input = input("Anda: ").lower()
        if user_input == "bye":
            print("Chatbot: Sampai jumpa!")
            break
        elif "halo" in user_input:
            print("Chatbot: Halo! Apa kabar?")
        elif "nama kamu siapa" in user_input:
            print("Chatbot: Saya adalah chatbot sederhana!")
        else:
            print("Chatbot: Maaf, saya belum mengerti.")


