import random
angka_rahasia = random.randint(1, 100)

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


angka = int(input("Tulis Sebuah Angka : "))
def tentukan_jenis_bilangan(angka):
    if angka > 0:
        return "Angka Positif"
    elif angka < 0:
        return "Angka Negatif"
    else:
        return "Angka Nol"
angka = float(input("Tulis Sebuah Angka: "))
hasil = tentukan_jenis_bilangan(angka)
print(hasil)