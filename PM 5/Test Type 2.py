#Percobaan 1
listkota=["Bogor","Bandung","Jakarta","Depok","Tangerang","Banten"]
for i,kota in enumerate(listkota):
    # print(i,kota)
    print("Indeks %d adalah kota %s" % (i,kota))

#Percobaan 2
for i in range(5):
    print("Pengulangan ke-",i)

#Percobaan 3
for i in range(5):
    print("Pengulangan ke-",i+1)

#Percobaan 4
for i in range(10,20+1):
    if(i==15):
        continue
    print(i)
    if(i==15):
        break
print("Selesai")

#Percobaan 5
listkota=["Bogor","Bandung","Jakarta","Depok","Tangerang","Banten"]
cari=input("Kota apa yang ingin dicari? ")
for index,kota in enumerate(listkota):
    # i/index pada kode diatas merupakan index dari list kota
    if kota.lower() == cari.lower():
        print("Kota %s terdapat pada indeks %d" % (cari,index))
        break
else:
    print("Maaf kota %s tidak ditemukan" % (cari))
print("Selesai")

#Percobaan 6
#while (1+2 == 3):
#    print("Halo Dunia!!")

#Percobaan 7
pencacah=5
while (pencacah<10):
    print(pencacah)
    pencacah+=1

#Percobaan 8
listkota=["Bogor","Bandung","Jakarta","Depok","Tangerang","Banten"]
i=0
while (i<len(listkota)):
    print(listkota[i])
    i+=1
  
#Percobaan 9
listkota=["Bogor","Bandung","Jakarta","Depok","Tangerang","Banten"]
while listkota:
    print(listkota.pop(0))

#Percobaan 10
password=("yukbisayuk")
kata=""
kata=input("Masukkan password: ")
while kata != password:
    print("password salah!")
    kata=input("Masukan password!")
print("password benar")


