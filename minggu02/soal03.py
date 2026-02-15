def main():
    gaji_per_jam = float(input("Masukkan gaji per jam yang dinginkan (dalam Rp): "))
    jam_kerja_per_minggu = float(input("Masukkan jumlah jam kerja yang dilakukan dalam 1 minggu: "))
    
    # Menghitung total pendapatan sebelum pajak
    total_jam_kerja = jam_kerja_per_minggu * 5  # 5 minggu
    pendapatan_sebelum_pajak = gaji_per_jam * total_jam_kerja
    
    # Menghitung pajak dan pendapatan setelah pajak
    pajak = 0.14 * pendapatan_sebelum_pajak
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak
    
    # Menghitung pengeluaran untuk baju, aksesoris, dan alat tulis
    uang_baju_aksesoris = 0.10 * pendapatan_setelah_pajak
    uang_alat_tulis = 0.01 * pendapatan_setelah_pajak
    
    # Menghitung sisa uang
    sisa_uang = pendapatan_setelah_pajak - (uang_baju_aksesoris + uang_alat_tulis)
    
    # Menghitung uang yang akan disedekahkan
    uang_disedekahkan = 0.25 * sisa_uang
    
    # Menghitung pembagian sedekah
    uang_anak_yatim = 0.30 * uang_disedekahkan
    uang_kaum_dhuafa = uang_disedekahkan - uang_anak_yatim
    
    # Output 
    print(f"\nPendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp {pendapatan_sebelum_pajak:.2f}")
    print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp {pendapatan_setelah_pajak:.2f}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {uang_baju_aksesoris:.2f}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {uang_alat_tulis:.2f}")
    print(f"Jumlah uang yang akan Budi sedekahkan: Rp {uang_disedekahkan:.2f}")
    print(f"Jumlah uang yang akan diterima anak yatim: Rp {uang_anak_yatim:.2f}")
    print(f"Jumlah uang yang akan diterima kaum dhuafa: Rp {uang_kaum_dhuafa:.2f}")

if __name__ == "__main__":
    main()