# Perhitungan Luas Bujur Sangkar
# Muhammad Zeinal Haq J0404241108

def input_nama():
    name = input("Masukkan nama lengkap anda: ")
    print("Selamat datang di SV IPB Class, " + name)
    return name

def input_penugasan():
    task = input("Ketik NIM untuk melanjutkan: ")
    print("Tugas Praktikum Prodas 2:")
    return task

def hitung_luas_bujur_sangkar():
    sisi = float(input("Masukkan panjang sisi bujur sangkar: "))
    luas = sisi ** 2
    print(f"Luas bujur sangkar dengan sisi {sisi} adalah: {luas}")

def main():
    name = input_nama()
    task = input_penugasan()
    hitung_luas_bujur_sangkar()

if __name__ == "__main__":
    main()
