#PR NO.1
def lulus_saja(data):
    siswa_lulus = [siswa['nama'] for siswa in data if siswa['nilai'] > 65]
    return siswa_lulus

#Data hasil_akhir
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

# Memanggil fungsi lulus_saja
siswa_lulus = lulus_saja(hasil_akhir)

#Menampilkan hasil
print("Siswa yang lulus:", siswa_lulus)

#PR NO.2
def balikan(daftar_buah):
    buah_terbalik = []
    for i in range(len(daftar_buah) - 1, -1, -1):
        buah_terbalik.append(daftar_buah[i])
    return buah_terbalik

#List buah-buahan
buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# Memanggil fungsi balikan
buah_terbalik = balikan(buah_buahan)

# Menampilkan hasil
print("Urutan terbalik dari buah-buahan:", buah_terbalik)

#PR NO.3
def duplikasi(daftar_buah):
    buah_terduplikasi = []
    for buah in daftar_buah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)
    return buah_terduplikasi

# List buah-buahan
buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# Memanggil fungsi duplikasi
buah_terduplikasi = duplikasi(buah_buahan)

# Menampilkan hasil
print("List dengan elemen terduplikasi:", buah_terduplikasi)

#PR NO.4
def nama(teks):
    j = ""
    for huruf in teks:
        if huruf.isalpha() and huruf.lower() not in 'aeiou':
            j += huruf
    return j

# String input
kalimat = "Nurul Fikri"

# Memanggil fungsi filter_konsonan
hasil = nama(kalimat)

# Menampilkan hasil
print("Konsonan dari string:", hasil)