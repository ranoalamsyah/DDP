#list
Honda=["cbr","cbr250",250,"hitam doff","rcb"]
Honda.append("60juta")
Honda.append("sport")
Honda.insert(2,"CBR250rr") 
print(Honda)

#match case
mtk=input("mau menghitung luas bangun datar apa?")
match mtk:
    case "persegi":
        s = int(input("masukan sisi: "))
        persegi = s*s
        print("luas persegi",persegi)
    case "lingkaran":
        r = int(input("masukan jari-jari: "))
        phi = 3.14
        lingkaran = phi*r*r
        print("luas lingkaran",lingkaran)
    case "segitiga":
        l = 1/2
        a = int(input("masukan alas: "))
        t = int(input("masukan tingi: "))
        segitiga = l*a*t
        print("luas segitiga",segitiga)
    case _:
        print("pilihan tidak tersedia")