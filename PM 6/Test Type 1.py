# Percobaan 1
list_kosong = []
list_buah = ["pisang", "nanas", "melon", "durian"]
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, "Presiden Sukarno", False]
print ("list kosong : ", list_kosong)
print ("list buah : ", list_buah)
print ("list nilai : ", list_nilai)
print ("list jawaban : ", list_jawaban)
print ("index list nilai pertama : ", list_nilai[0])
print ("index list jawaban terakhir : ", list_jawaban[3])
print ("index list buah terakhir : ", list_buah[-1])

# Percobaan 2
list_kosong = []
list_buah = ["pisang", "nanas", "melon", "durian"]
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, "Presiden Sukarno", False]
print ("list pemotongan : ", list_jawaban[1:-2])
list_nilai = list_nilai[1:-1]
print ("isi list nilai: ", list_nilai)

# Percobaan 3
list_kosong = []
list_buah = ["pisang", "nanas", "melon", "durian"]
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, "Presiden Sukarno", False]
list_jawaban[2] = "Bandung"
print ("list jawaban : ", list_jawaban)
list_jawaban.append("baju baru")
print("isi list jawaban setelah append : ", list_jawaban)
list_jawaban.insert(2,1945)
print ("list campur setelah insert dan append : ", list_jawaban)

# Percobaan 4
list_kosong = []
list_buah = ["pisang", "nanas", "melon", "durian"]
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, "Presiden Sukarno", False]
#pop berfungsi menghapus item terakhir
list_buah.pop()
list_buah.pop()
print ("isi list buah setelah pop 2 kali : ", list_buah)
#remove berfungsi menghapus item sesuai variabel yang dipiih
list_buah.remove("nanas")
print ("isi list buah setelah remove nanas : ", list_buah)

# Percobaan 5
list_kosong = []
list_buah = ["pisang", "nanas", "melon", "durian"]
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, "Presiden Sukarno", False]
#urutkan secara ascending
list_buah.sort()
print (list_buah)
#membalikkan posisi item list (tidak harus berurut)
list_buah.reverse()
print (list_buah)

# Percobaan 6
#Tuple sama saja dengan list. Dia sama-sama digunakan untuk menyimpan data himpunan.  Sama-sama  bisa  menampung  berbagai  macam  tipe  data  dalam  satu  himpunan.  Hanya  saja setelah diberi nilai, tuple tidak bisa diubah lagi. Hal ini berbeda dengan list.
#cara standar 
tuple_jenis_kelamin = ('laki-laki', 'perempuan')
#tanpa kurung 
tuple_status_perkawinan = 'menikah', 'lajang'
#menggunakan fungsi tuple() 
tuple_lulus = tuple(['lulus', 'tidak lulus'])