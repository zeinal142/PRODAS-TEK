#membuat barisan angka
jangkauan = int(input('masukkan angka'))
hasil = ""
n = 1

for i in range(1,jangkauan + 1) :
    hasil += str(n)
    print(hasil)
    n += 1

#tahun kabisat
tahun = int(input('masukkan tahun'))

if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0 :
    print('adalah tahun kabisat')
else :
    print('bukan tahun kabisat')

#bilangan faktorial
angka = int(input('masukkan angka'))
faktorial = 1

for i in range(1, angka + 1) :
    faktorial = faktorial * i
print(faktorial)

#mencari nilai dalam list
list1 = [10, 20, 30, [200, 300, [5000,6000], 400], 30, 40]
print(list1 [3][2])
print(list1 [5])
list1[3][2].insert(1,7000)
print(list1)
print(list1[5])

#deret fibonacci
n = int(input('masukkan angka'))
listFibonacci = []
a, b = 0, 1

for i in range(0, n+1):
    a, b = b, a + b
    listFibonacci.append(a)
    print(f'List Fibonacci = {a}')

if n not in listFibonacci:
    print(f'{n} bukan fibonacci')
else:
    print(f'{n} merupakan fibonacci')   

#akar sempurna
bilangan = int(input('masukkan angka'))

akar = bilangan ** 0.5

if akar == int(akar) :
    print('akar sempurna')
else :
    print('bukan')
