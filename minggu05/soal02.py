def cek_digit_belakang(a, b, c):
    a1 = a % 10
    b1 = b % 10
    c1 = c % 10

    if (a1 == b1) or (a1 == c1) or (b1 == c1):
        return True
    else:
        return False

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

print("Hasil:", cek_digit_belakang(a, b, c))