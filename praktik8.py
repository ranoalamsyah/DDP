#Deklarasi fungsi
def hello():
    print("hallo saya STT Terpadu Nurul Fikri")
    print("saya Program Studi Teknik Informatika")
#Memanggi fungsi
hello()
hello()
#
def say(nama, prodi):
    print("halo nama saya adalah", nama)
    print("prodi saya adalah", prodi)
#
say("ahmad" , "SI")
#
def jumlah(a,b):
    jumlah=a+b
    print(jumlah)
jumlah(3,5)

#
def pengali(x):
    return x*2

def hitungluas(sisi):
    luas = (sisi*sisi)
    return luas

def pangkat(a,b):
    return a**b
#memanggil fungsi
print(pengali(5))
print("luas persegi adalah" ,hitungluas(5))
print(pangkat(2,3))