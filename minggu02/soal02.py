def f(x):
    return 2 * (x ** 3) + 2 * x + (15 / x)

def main():
    try:
        x = int(input("Masukkan bilangan: "))
        if x == 0:
            print("Bilangan tidak boleh 0.")
        else:
            hasil = f(x)
            print(f"Hasil dari f({x}) = {hasil}")
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

if __name__ == "__main__":
    main()