#day11
#RPL
#belajar menyelesaikan contoh kasus
#harga bolpoin = 1750
#uang ardi 5000 * 5 lembar

harga_bolpoin = int (input ("masukkan harga satu buah bolpoin : "))
selusin_bolpoin = int (input ("jumlah isi bolpoin dlm selusin : "))
uang_diberikan = int (input ("jumlah uang yang diberikan : "))
harga_selusin = selusin_bolpoin * harga_bolpoin

if selusin_bolpoin == 12:
    uang_kembalian = uang_diberikan - harga_selusin
    print ("uang kembalian Ardi : Rp. " , uang_kembalian)
