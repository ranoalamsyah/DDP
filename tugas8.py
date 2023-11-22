#Deklarasi fungsi
def profil(nama ,alamat ,gender ,umur ,hoby):
    print("halo nama saya" ,nama)
    print("saya tinngal di" ,alamat)
    print("saya adalah seorang" ,gender)
    print("saya berumur" ,umur)
    print("saya mempunyai hoby" ,hoby)
#
profil("Rano Alamsyah" , "jalan mujair dalam,pasar minggu" , "laki-laki" , "19 tahun" , "Bermain game")

#Deklarasi fungsi 2
def nilai_kelulusan(kelulusan):
    if(kelulusan <= 60):
        print("Gagal")
    elif(kelulusan >=61 and kelulusan <=70):
        print("Baik")
    elif(kelulusan >=71 and kelulusan <=80):
        print("Sangat Baik")
    elif(kelulusan >=81 and kelulusan <=100):
        print("istimewa")
    else:
        print("pilihan tidak ada")
#
nilai_kelulusan(85)

#
def angka(ganjil):
    for j in range(ganjil):
        if (j %2 !=0):
            print(j, end=' ') 

#
angka(100)