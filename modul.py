import math

#Perhitungan
def tambah(bil1, bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)
def log(bil1, bil2):
    hasil = math.log(bil1, bil2)
    print("hasil log dari",bil1,"log", bil2,"=",hasil)
def akar(bil1):
    hasil = math.sqrt(bil1)
    print("hasil akar dari",bil1,"=",hasil)
def sin(bil1):
    hasil = math.sin(bil1)
    print("hasil sin dari",bil1,"=",hasil)
def cos(bil1):
    hasil = math.cos(bil1)
    print("hasil cos dari",bil1,"=",hasil)
def tan(bil1):
    hasil = math.tan(bil1)
    print("hasil tan dari",bil1,"=",hasil)

#Bangun datar
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_persegi(sisi):
    return sisi * sisi
def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2
def keliling_belah_ketupat(sisi):
    return 4 * sisi

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi
def keliling_jajar_genjang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2

def keliling_layang_layang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)