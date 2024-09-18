# Perhitungan Operasi Bitwise XOR
# Muhammad Zeinal Haq J0404241108

def input_nama():
    name = input("Masukkan nama lengkap anda: ")
    print("Selamat datang di SV IPB Class, " + name)
    return name

def input_penugasan():
    task = input("Ketik NIM untuk melanjutkan: ")
    print("Tugas Praktikum Prodas 2:")
    return task

def hitung_operasi_bitwise():
    a = int(input("Masukkan Bilangan ke-1: "))
    b = int(input("Masukkan Bilangan ke-2: "))
    print(f'{a} ^ {b} = {a ^ b}')
    print(f'format(a, "08b") ^ format(b, "08b") = {format(a ^ b, "08b")}')

def main():
    name = input_nama()
    task = input_penugasan()
    hitung_operasi_bitwise()

if __name__ == "__main__":
    main()
