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