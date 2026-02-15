def print_matrix(tinggi, lebar):
    count = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(count, end=' ')
            count += 1
        print()

try:
    tinggi = int(input("Masukkan tinggi: "))
    lebar = int(input("Masukkan lebar: "))
    if tinggi <= 0 or lebar <= 0:
        print("Tinggi dan lebar harus bilangan positif.")
    else:
        print_matrix(tinggi, lebar)
except ValueError:
    print("Masukkan angka yang valid!")
