import sys

# Simulasi database tugas mahasiswa
database_tugas = {
    "J0404241108": ["Tugas Matematika", "Tugas Fisika"],
    "J0404241109": ["Tugas Kimia", "Tugas Biologi"],
    "J0404241110": ["Tugas Sejarah"],
    "J0404241111": ["Tugas Geografi"],
    "J0404241112": ["Tugas Matematika", "Tugas Geografi"],
    "J0404241113": ["Sudah Selesai Semua!!"],
}

def input_usia():
    age = int(input("Masukkan usia Anda: "))
    if age >= 18:
        print("Anda merupakan seorang Mahasiswa.")
        return age
    else:
        print("Anda masih di bawah umur, mohon maaf.")
    sys.exit()  # Menghentikan program jika usia di bawah 18 tahun


def input_nama():
    name = input("Masukkan nama lengkap anda: ")
    print("Selamat datang di SV IPB Class, " + name)
    return name

def input_nim():
    number = input("Masukkan NIM anda: ")
    print("NIM " + number)
    return number

def cek_penugasan(number):
    if number in database_tugas:
        tugas_belum_dikerjakan = database_tugas[number]
        if tugas_belum_dikerjakan:
            print(f"Tugas yang belum dikerjakan oleh {number}:")
            for tugas in tugas_belum_dikerjakan:
                print(f"- {tugas}")
        else:
            print(f"{number} tidak memiliki tugas yang belum dikerjakan. Selamat!")
    else:
        print(f"NIM {number} tidak ditemukan dalam database.")

def main():
    age = input_usia()
    name = input_nama()
    number = input_nim()
    cek_penugasan(number)

if __name__ == "__main__":
    main()