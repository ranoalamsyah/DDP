#if 1
namabarang="keset"
hargabarang=99000

if(hargabarang > 99000): 
    keterangan ="anda mendapat sapu tangan"

else: 
    keterangan ="terima kasih sudah beli keset"

print("namabarang", namabarang, "\nharga barang anda Rp. ", hargabarang, "\n", keterangan)

#if 2
nama="setiawan"
matkul="mtk"
Nilai=30.33
keterangan ="lulus" if Nilai >=75 else "gagal"

print("nama\t:",nama,"\nmata kuliah\t:",matkul,"\nNilai\t\t:",Nilai,"\nketerangan\t:",keterangan)

#if 3
Nama="budi santoso"
matpel="matematika komputer"
nilai=59.99
#uji grade dengan if multi kondisi
if(nilai >= 85 and nilai <=100) : 
    grade="A"
elif(nilai >= 75 and nilai <=85) : 
    grade="B"
elif(nilai >= 60 and nilai <=75) : 
    grade="C"
elif(nilai >= 30 and nilai <=60) : 
    grade="D"
else: 
    grade="E"
print("Nama\t:",Nama,"\nmata pelajaran\t:",matpel,"\nnilai\t\t:",nilai,"\ngrade\t:",grade)