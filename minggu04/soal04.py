while True:
    try:
        sisi1 = float(input("Masukkan sisi 1: "))
        sisi2 = float(input("Masukkan sisi 2: "))
        sisi3 = float(input("Masukkan sisi 3: "))

        if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
            print("Panjang sisi harus lebih dari 0!")
            continue

        if sisi1 == sisi2 == sisi3:
            print("3 sisi sama")
        elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
            print("2 sisi sama")
        else:
            print("Tidak ada yang sama")

        break

    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")