# Soal 6
import random
angka_rahasia = random.randint (1,100)

print("========================================")
print("Kami telah memiliki angka, silakan tebak!")
print("========================================")

while True:
    tebakan = int(input("Masukkan angka: "))
    
    if tebakan > angka_rahasia:
        print("Tebakanmu terlalu besar")
    elif tebakan < angka_rahasia:
        print("Tebakanmu terlalu kecil")
    else:
        print("Selamat, tebakanmu benar!")
        break
