#belajarpenggunaanUPPER()
#day27

harga = int (input ("masukkan harga hp = Rp. "))
kode_promo = input ("masukkan kode promo = ")
kode_promo = kode_promo.upper()

if kode_promo == "DISKONOPPO":
	diskon = harga * 40/100
elif kode_promo == "DISKONVIVO" :
	diskon = harga * 45/100
elif kode_promo == "DISKONXIOMI":
	diskon = harga * 60/100
else :
	diskon = 0
	print ("diskon merk hp tidak ada")
	
lastpay = harga - diskon
print ("diskon hari ini " , kode_promo)
print ("jumlah diskon " , diskon)
print ("pembayaran = Rp. " , lastpay)