# Soal 2
def hitung_diskon(kode, harga):
    if kode == 1:  # Barang baru
        diskon = 0.10
    elif kode == 2:  # Barang lama
        if harga <= 50000:
            diskon = 0.15
        elif harga <= 200000:
            diskon = 0.20
        else:
            diskon = 0.25
    else:
        return "Kode barang tidak valid"
    
    harga_setelah_diskon = harga * (1 - diskon)
    return harga_setelah_diskon

kode = int(input("Barang apakah yang anda beli? (ketik 1 untuk barang baru, ketik 2 untuk barang lama): "))
harga = float(input("Harga barang sebelum diskon (dalam rupiah): "))
harga_setelah_diskon = hitung_diskon(kode, harga)
print(f"Harga yang harus dibayarkan (dalam rupiah): {harga_setelah_diskon:.2f}")
