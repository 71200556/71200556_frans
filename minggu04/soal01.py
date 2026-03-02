# latihan 3.1
while True:
    inputuser = input("Masukkan sebuah bilangan: ")

    try:
        angka = int(inputuser)

        if angka <= 1:
            print("Bukan bilangan prima")
        else:
            prima = True
            for i in range(2, angka):
                if angka % i == 0:
                    prima = False
                    break

            if prima:
                print("Bilangan Prima")
            else:
                print("Bukan Bilangan Prima")

        break

    except ValueError:
        print("Input harus berupa angka bulat!")

# latihan 3.2
try:
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))

    D = b**2 - 4*a*c

    if D > 0:
        print("Akar Real dan Berlainan")
    elif D == 0:
        print("Akar Real dan Kembar")
    else:
        print("Akar Imajiner / Tidak Real")

except ValueError:
    print("Input harus berupa angka!")

# latihan 3.3
while True:
    inputuser = input("Masukkan bilangan untuk dihitung faktorial: ")

    try:
        n = int(inputuser)

        if n < 0:
            print("Bilangan tidak boleh negatif!")
            continue

        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i

        print("Nilai faktorial =", faktorial)
        break

    except ValueError:
        print("Input harus berupa angka bulat!")
        