name = input("Masukkan nama lengkap anda: ")
print("Selamat datang di SV IPB Class, " + name)

name = input("Ketik 'Oke' untuk melanjutkan: ")
print("Tugas Praktikum Prodas 2:")

# Meminta pengguna untuk menginput empat bilangan bulat
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
bilangan4 = int(input("Masukkan bilangan keempat: "))

# Menggunakan operator penugasan untuk menjumlahkan bilangan
jumlah = 0
jumlah += bilangan1
jumlah += bilangan2
jumlah += bilangan3
jumlah += bilangan4

# Menampilkan hasil
print("Jumlah dari keempat bilangan adalah:", jumlah)

# Meminta pengguna untuk menginput empat bilangan bulat
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
bilangan4 = int(input("Masukkan bilangan keempat: "))

# Menggunakan operator penugasan untuk menjumlahkan bilangan
terbesar = max(bilangan1, bilangan2, bilangan3, bilangan4)
terkecil = min(bilangan1, bilangan2, bilangan3, bilangan4)

# Menampilkan hasil
print("Urutan angka dari terbesar:", terbesar)
print("Urutan angka dari terkecil:", terkecil)

import math

def hitung_luas_lingkaran():
    radius = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * radius ** 2
    print(f"Luas lingkaran dengan jari-jari {radius} adalah: {luas}")

def hitung_luas_bujur_sangkar():
    sisi = float(input("Masukkan panjang sisi bujur sangkar: "))
    luas = sisi ** 2
    print(f"Luas bujur sangkar dengan sisi {sisi} adalah: {luas}")

def hitung_luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah: {luas}")

# Menu untuk memilih bangun datar
def menu():
    while True:
        print("\nPilih bangun datar untuk dihitung luasnya:")
        print("1. Lingkaran")
        print("2. Bujur Sangkar")
        print("3. Segitiga")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            hitung_luas_lingkaran()
        elif pilihan == '2':
            hitung_luas_bujur_sangkar()
        elif pilihan == '3':
            hitung_luas_segitiga()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        # Menanyakan apakah ingin melakukan perhitungan lain
        lagi = input("Apakah Anda ingin menghitung luas bangun datar lain? (y/n): ")
        if lagi.lower() != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break

# Memanggil menu
menu()
