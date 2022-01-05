#belajar nested if
harga_tanah_permeter = 300000
harga_jual = int(input('masukan harga jual : '))
luas_tanah = int(input('masukan luas tanah : '))

if harga_jual >= 100000000 :
	print ('anda di kenakan pajak 5%')
	potongan = harga_tanah_permeter* 5/100
	gaji_bersih = harga_jual -potongan
else:
	if harga_jual >= 50000000 :
		print ('anda di kenakan pajak 3%')
		potongan = harga_tanah_permeter *3/100
		gaji_bersih = harga_jual - potongan
	else:
		print('anda dikenakan pajak 1%')
		potongan = harga_tanah_permeter *1/100
		gaji_bersih = harga_jual - potongan
	
print (potongan)	
print ('kamu harus membayar sebesar, Rp. ', gaji_bersih)