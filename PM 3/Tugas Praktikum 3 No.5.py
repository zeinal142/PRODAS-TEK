#Tugas 5
name = input("Masukkan nama lengkap anda: ")
print("Selamat datang di SV IPB Class, " + name)
task = input("Ketik NIM untuk melanjutkan: ")
print("Penugasan Dasar Pemrograman No.5")
a = 18
b = 10
day = 3
condition1 = (3 == 3) and (a > b)
print("Condition 1:", condition1)
condition2 = (3 != 3) and (a >= b)
print("Condition 2:", condition2)
condition3 = (3 >= 4) and (a >= 18 and day == 3)
print("Condition 3:", condition3)
condition4 = not (3 < 4) and (a >= 18 or day != 3)
print("Condition 4:", condition4)