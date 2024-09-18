# Soal 4
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