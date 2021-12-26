#day14
#RPL
#uji kembali operator logika

penghasilan = int (input ("penghasilan tiap bulan : "))
pekerjaan = input ("masukkan pekerjaan : ")
if penghasilan >= 5000000 and pekerjaan == "pns":
    pajak = 10/100 + 5/100 * penghasilan
    print ("pajak 15%")
    gaji_bersih = penghasilan - pajak
    print ("gaji bersih perbulan : Rp. " , gaji_bersih)
elif penghasilan >= 3000000 and pekerjaan == "pns":
    pajak = 5/100 + 5/100 * penghasilan
    print ("pajak 10%")
    gaji_bersih = penghasilan - pajak
    print ("gaji bersih perbulan : Rp. " , gaji_bersih)
else:
    print ("anda tidak dikenakan pajak ")
    print ("gaji bersih : Rp. " , penghasilan)
    
