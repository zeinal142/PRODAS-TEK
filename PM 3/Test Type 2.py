# Tugas 1
print ("TUGAS 1")
a=2
b=3
c=4
print(a<b<=c)
print(a==b==c)
print(a!=b!=c)
print(str(a) + "kali")
print((a) * "kali")

#Tugas 2
print ("TUGAS 2")
True and False
False or True
1 == 1 and 2 == 1
"true" == True
False and 0!= 0
not (10 == 1 or 1000 == 1000)
"pete" == "jengkol" and (not (3 == 4 or 3 == 3))
3 == 3 and not ("test" == "test" or "Python" == "Fun")
print(True and False)
print(False or True)
print(1 == 1 and 2 == 1)
print("true" == True)
print(False and 0!= 0)
print(not (10 == 1 or 1000 == 1000))
print("pete" == "jengkol" and (not (3 == 4 or 3 == 3)))
print(3 == 3 and not ("test" == "test" or "Python" == "Fun"))

#Tugas 3
print ("TUGAS 3")
True
3 == 4
3 + 4
3 + 4 == 7
"False"
print(bool(True))
print(bool(3 == 4))
print(bool(3 + 4))
print(bool(3 + 4 == 7))
print(bool("False"))

#Tugas 4
print ("TUGAS 4")
if 4+5 == 10: 
    print("TRUE")
else:
    print("FALSE") 
print("TRUE")

if 4+5 == 10: 
    print("TRUE")
else: 
    print("FALSE")

#Tugas 5
print ("TUGAS 5")
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

#Tugas 6
print ("TUGAS 6")
huruf = str(input('masukan huruf vokal: '))
vokal = ['a', 'i', 'u', 'e', 'o']
if huruf in vokal:
    print("huruf", huruf, "adalah huruf vokal")
else:
    print('huruf', huruf, "bukan huruf vokal")

#Tugas 7
print ("TUGAS 7")
a = int(input('Masukkan integer pertama: '))
b = int(input('Masukkan integer kedua: '))
if a == 7 or b == 7 :
    print('Hasil : benar')
elif a + b == 7 :
    print('Hasil : benar')
elif abs(a - b) == 7 :
    print('Hasil : benar')
else:
    print('salah')

#Tugas 8
print ("TUGAS 8")
import math

def cari_akar(a, b, c):
    d = b**2 - 4*a*c

    if d < 0:
        return "Tidak ada akar real"
    elif d == 0:
        x = -b / (2*a)
        return f"Akar tunggal: {x}"
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Akar pertama: {x1}, Akar kedua: {x2}"

a = int(input("Masukkan untuk nilai A: "))
b = int(input("Masukkan untuk nilai B: "))
c = int(input("Masukkan untuk nilai C: "))

hasil = cari_akar(a, b, c)
print(hasil)