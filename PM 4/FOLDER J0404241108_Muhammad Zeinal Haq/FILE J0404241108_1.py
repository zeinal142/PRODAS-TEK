# Soal 1
harga_pokok = int(input("Harga Pokok Barang : "))
harga_jual = int(input("Harga Jual Barang : "))

keuntungan = harga_jual / harga_pokok * 100 - 100
print("Keuntungan Penjualan adalah : {:.2f}".format(keuntungan),"%")