#day21
#RPL
#belajar menyelesaikan kasus

hargapersemen = int (input ("masukkan harga satu semen : "))
dibeli = int (input ("masukkan maks semen yg dibeli : "))
hargamaks = dibeli * hargapersemen
if dibeli == 100 :
    potongan = hargamaks * 2.5/100
elif dibeli > 200 :
    potongan = hargamaks * 10/100
else :
    potongan = hargamaks * 0
    print ("tidak dapat potongan")

pembayaran = hargamaks - potongan
print ("jumlah pembayaran : Rp. " , pembayaran)
print ("harga keseluruhan semen yang dibeli : Rp " , format(hargamaks))
print ("potongan yg didapat : Rp. " , format(potongan))
