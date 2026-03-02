while True:
    inputuser = input("Masukkan bulan (1-12): ")

    try:
        bulan = int(inputuser)

        if bulan < 1 or bulan > 12:
            print("Bulan yang diinputkan tidak valid!")
            continue

        if bulan == 2:
            jumlah_hari = 29  # Tahun 2020 (kabisat)
        elif bulan in [4, 6, 9, 11]:
            jumlah_hari = 30
        else:
            jumlah_hari = 31

        print("Jumlah hari:", jumlah_hari)
        break

    except ValueError:
        print("Input harus berupa angka antara 1 sampai 12!")