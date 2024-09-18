import sys

def input_nama():
    name = input("Masukkan nama Anda: ")
    print("Selamat datang di SV IPB Class, " + name)
    return name

def input_usia():
    while True:
        try:
            age = int(input("Masukkan usia Anda: "))
            if age < 0:
                raise ValueError("Usia tidak boleh negatif.")
            return age
        except ValueError as e:
            print(e)

def cek_usia(age):
    if age >= 18:
        print("Anda merupakan seorang Mahasiswa.")
    else:
        print("Anda masih di bawah umur, mohon maaf.")
        sys.exit()

def input_penugasan():
    while True:
        try:
            penugasan = int(input("Tuliskan kode belajar anda: "))
            if penugasan < 0:
                raise ValueError("Kode belajar tidak boleh negatif.")
            return penugasan
        except ValueError as e:
            print(e)

def cek_penugasan(penugasan):
    if penugasan >= 5:
        print('Tugas anda lebih dari 5, coba lebih rajin ya')
    else:
        print('Selamat tugas anda tinggal sedikit, Semangat!!')

def main():
    name = input_nama()
    age = input_usia()
    cek_usia(age)
    penugasan = input_penugasan()
    cek_penugasan(penugasan)

if __name__ == "__main__":
    while True:
        main()
        ulangi = input("Apakah Anda ingin mengulangi proses? (y/n): ")
        if ulangi.lower() != 'y':
            break