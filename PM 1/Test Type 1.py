import sys

# Simulasi database tugas mahasiswa
database_tugas = {
    "Zeinal": ["Tugas Matematika", "Tugas Fisika"],
    "Yoseph": ["Tugas Kimia", "Tugas Biologi"],
    "Dandi": ["Tugas Sejarah", "Tugas Geografi"]
}

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

def input_kode_tugas():
    kode_tugas = input("Masukkan NIM anda sebagai identitas mahasiswa IPB: ")
    print(f"Kode tugas Anda adalah: {kode_tugas}")
    return kode_tugas

def cek_penugasan(nama):
    if nama in database_tugas:
        tugas_belum_dikerjakan = database_tugas[nama]
        if tugas_belum_dikerjakan:
            print(f"Tugas yang belum dikerjakan oleh {nama}:")
            for tugas in tugas_belum_dikerjakan:
                print(f"- {tugas}")
        else:
            print(f"{nama} tidak memiliki tugas yang belum dikerjakan. Selamat!")
    else:
        print(f"Nama {nama} tidak ditemukan dalam database.")

def main():
    name = input_nama()
    age = input_usia()
    cek_usia(age)
    kode_tugas = input_kode_tugas()
    cek_penugasan(name)

if __name__ == "__main__":
    while True:
        main()
        ulangi = input("Apakah Anda ingin mengulangi proses? (y/n): ")
        if ulangi.lower() != 'y':
            break
