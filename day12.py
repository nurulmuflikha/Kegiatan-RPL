#day12
#RPL
#operator logika
#and, or , not


print ("nomor 1")
gaji = int (input ("masukkan gaji : "))

if gaji >= 20000000:
    print ("dikenakan pajak 5%")
    pajak =  gaji * 5/100
    print ("pajak : " , pajak)
    jml_gaji =  gaji - pajak
    print ("jumlah gaji : Rp. " , jml_gaji)
elif gaji >= 10000000 :
    print ("dikenakan pajak 2%")
    pajak =  gaji * 2/100
    print ("pajak : " , pajak)
    jml_gaji =  gaji - pajak
    print ("jumlah gaji : Rp. " , jml_gaji)
else :
    print ("tidak dikenakan pajak")

print ("nomor 2")
gaji = int (input ("masukkan gaji : "))
kerja = input ("masukkan pekerjaan : ")

if gaji >= 10000000 and kerja == "pns":
    print ("dikenakan pajak")
    pajak =  2/100 + 3/100 * gaji
    print ("pajak : " , pajak)
    jml_gaji =  gaji - pajak
    print ("jumlah gaji : Rp. " , jml_gaji)
elif gaji >= 20000000 and kerja == "pns":
    print ("dikenakan pajak")
    pajak =  5/100 + 3/100 * gaji
    print ("pajak : " , pajak)
    jml_gaji =  gaji - pajak
    print ("jumlah gaji : Rp. " , jml_gaji)
else :
    print ("tidak dikenakan pajak")
