# penugasan pertama

a = 10
print('a = 10 -> ', a)

a += 5
print('a += 5 -> ', a)

a -= 3
print('a -= 3 -> ', a)

a *= 6
print('a *= 6 -> ', a)

a /= 8
print('a /= 8 -> ', a)

# a = float, kita ubah jadi integer
a = int(a)

a %= 9
print('a %= 9 -> ', a)

a //= 6
print('a //= 6 -> ', a)

a **= 1
print('a **= 1 -> ', a)

a &= 2
print('a &= 2 -> ', a)

a |= 3
print('a |= 3 -> ', a)

a ^= 4
print('a ^= 4 -> ', a)

a >>= 4
print('a >>= 4 -> ', a)

a <<= 4
print('a <<= 4 -> ', a)

universitas = 'IPB'
list_pulau = ['Jawa', 'Sumatra', 'Sulawesi']

mahasiswa = {
    'nama': 'Muhammad Zeinal Haq',
    'asal': 'Jawa'
}

print(
    "Apakah 'I' ada di variabel universitas?",
    'I' in universitas
)