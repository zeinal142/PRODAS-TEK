#Tugas 1
def generate_fibonacci():
    n = int(input("Masukkan panjang deret fibonacchi yang diinginkan: "))
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

fib_sequence = generate_fibonacci()
print(fib_sequence)

# Tugas 2
def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    while True:
        n = int(input("Masukkan angka yang ingin dicek (masukkan 0 untuk keluar): "))
        if n == 0:
            break
        if check_prime(n):
            print(f"{n} adalah bilangan prima.")
        else:
            print(f"{n} bukan bilangan prima.")

main()

#Tugas 3
def count_vowels(string):
    vowels = "aeiou"  # Hapus .lower di sini karena vowels sudah dalam huruf kecil
    count = 0
    for char in string:
        if char.lower() in vowels:  # Pastikan untuk mengubah karakter menjadi huruf kecil
            count += 1
    return count

def count_vowels_in_string():
    string = input("Masukkan huruf yang ingin dicari vokalnya: ")
    vowel_count = count_vowels(string)
    print(f"Jumlah huruf vokal dalam '{string}' adalah {vowel_count}.")

count_vowels_in_string()

#Tugas 4
def calculate_power():
    base = int(input("Masukkan bilangan dasar: "))
    exponent = int(input("Masukkan pangkat: "))
    result = 1
    for _ in range(exponent):
        result *= base
    print(f"{base} pangkat {exponent} adalah {result}")

calculate_power()

#Tugas 5
def replace_vowels(string, replacement_char):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char in vowels:
            result += replacement_char
        else:
            result += char
    return result

def replace_vowels_in_string():
    string = input("Masukkan kata atau kalimat: ")
    replacement_char = input("Masukkan karakter pengganti vokal: ")
    new_string = replace_vowels(string, replacement_char)
    print(f"Hasil penggantian vokal: {new_string}")

replace_vowels_in_string()
