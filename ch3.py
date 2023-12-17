numbers = [1,2,4,5,100,10]
print(numbers[3]) #indexing
print(numbers[1:4]) # slicing
#
numbers =[]
print(numbers)
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
a = numbers.pop()
print(a)
print(numbers)
#
names = {"apel", "mangga", "pisang", "jambu"}
#print(names)

list_name = []
for name in names:
    list_name.append(name)
print(list_name)

numbers = {9,9,6,8,1,3,2}
print(numbers)
#
null_set = set()
null_set.add(1) #menambahkan data ke dalam set
print(null_set)
#menggabungkan dengan union
set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)
#memasukan dengan update
set1 = {1,2,3}
set2 = {2,4,8}
set1.update(set2)
print(set1)

#dictionary
#mahasiswa = {
#    "nama":"banjo",
#    "semester": 1,
#    "hobi": ["mancing", "membaca", "nyolong"]
#}

#print(mahasiswa["semester"][0])

data = {
    "mhs" : {
        "nama":"banjo",
        "semester": 1,
        "hobi": ["mancing", "membaca", "nyolong"],
        "pacar" : {
            "nama": ["lala", "lili", "lulu", "lele"],
            "selingkuhan" : {
                "nama" : ["igun", "ical", "mikel", "acam"]            
            }
        }
    },
    "dosen": {
        "Nama" : "Reza maulana",
        "Alamat" : "Beji",
    }
}
data["mhs"]["semester"] = 2
print(data["mhs"]["semester"])