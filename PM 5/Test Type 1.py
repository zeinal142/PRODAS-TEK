# Pengetesan Login dengan Password
password = str("zeinal142")

while True:
    masukan = str(input("Masukkan password: "))
    
    if masukan != password:
        print("Password Kamu Salah")
    else:
        print("Password Kamu Benar!")
        break