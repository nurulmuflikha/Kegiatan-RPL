#menampilkan tabel perkalian
#num = angka
#multiplication table of = kalimat bhs inggris

num = int(input("Multiplication table of: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)