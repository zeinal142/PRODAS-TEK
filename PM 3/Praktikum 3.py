# Perhitungan Nilai Anda

def input_nama():
    name = input("Masukkan nama lengkap anda: ")
    print("Selamat datang di SV IPB Class, " + name)
    return name

def input_nim():
    task = input("Ketik NIM untuk melanjutkan: ")
    print("Input Nilai Semester 1")
    return task

def input_uts():
    uts = float(input("NIlai UTS: "))
    return uts

def input_utsp():
    utsp = float(input("NIlai UTSP: "))
    return utsp

def input_uas():
    uas = float(input("NIlai UAS: "))
    return uas

def input_uasp():
    uasp = float(input("NIlai UASP: "))
    return uasp

def perhitungan_nilai_akhir(uts, utsp, uas, uasp):
    nilai_akhir = uts * 0.3 + utsp * 0.15 + uas * 0.4 + uasp * 0.15
    print(f"Nilai akhir: {nilai_akhir}")
    return nilai_akhir
    
def nilai_keluaran(nilai_akhir):
    if 80 <= nilai_akhir <= 100:
        print("Predikat Nilai Kamu A")
    elif 70 <= nilai_akhir < 80:
        print("Predikat Nilai Kamu B")
    elif 60 <= nilai_akhir < 70:
        print("Predikat Nilai Kamu C")
    elif 40 <= nilai_akhir < 60:
        print("Predikat Nilai Kamu D")
    elif 0 <= nilai_akhir < 40:
        print("Predikat Nilai Kamu E")
    else : 
        print("invalid")
    return nilai_akhir
    
def main():
    name = input_nama()
    task = input_nim()
    uts = input_uts()
    utsp = input_utsp()
    uas = input_uas()
    uasp = input_uasp()
    nilai_akhir = perhitungan_nilai_akhir(uts, utsp, uas, uasp)
    nilai_keluaran(nilai_akhir)
    
if __name__ == "__main__":
    main()