# Menerima input dari pengguna
bil1 = float(input("Masukkan angka : "))
bil2 = float(input("Masukkan angka : "))
operator = input("Pilih operator (+, -, *, /, **): ")

# Proses perhitungan sesuai operator
if operator == '+':
    hasil = bil1 + bil2
    keterangan_operator = "Tambah"
elif operator == '-':
    hasil = bil1 - bil2
    keterangan_operator = "Kurang"
elif operator == '*':
    hasil = bil1 * bil2
    keterangan_operator = "Kali"
elif operator == '/':
    # Menangani pembagian dengan nol
    if bil2 == 0:
        print("Error: Pembagian dengan nol tidak diizinkan.")
    else:
        hasil = bil1 / bil2
        keterangan_operator = "Bagi"
elif operator == '**':
    hasil = bil2 ** bil2
    keterangan_operator = "Pangkat"
else:
    print("Error: Operator tidak valid.")
    exit()  # Keluar dari program jika operator tidak valid

# Menampilkan hasil perhitungan
print(f"\nAngka pertama: {int(bil1)}")
print(f"Angka kedua: {int(bil2)}")
print(f"Pilihan Operator: {keterangan_operator}")
print(f"Hasil operator: {int(bil1)} {operator} {int(bil2)} = {int(hasil)}")





# Menerima input dari pengguna
sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

# Menghitung luas trapesium
luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi

# Menghitung keliling trapesium
keliling = sisi_atas + sisi_bawah + 2 * sisi_miring

# Menampilkan hasil perhitungan
print(f"\nLuas Trapesium: {int(luas)}")
print(f"Keliling Trapesium: {int(keliling)}")