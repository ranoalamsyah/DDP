#Start
#Input Panjang Sisi Atas
#Input Panjang Sisi Bawah
#Input Panjang Sisi Miring
#Input Tinggi
# Menghitung luas trapesium
#Luas = 0.5 * (Sisi_Atas + Sisi_Bawah) * Tinggi
# Menghitung keliling trapesium
#Keliling = Sisi_Atas + Sisi_Bawah + 2 * Sisi_Miring
#Display "Luas Trapesium:", Luas
#Display "Keliling Trapesium:", Keliling
#End

#Menerima input dari pengguna
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