#day18
#RPL
#belajar percabangan

hutang = int (input ("masukkan hutang = Rp. "))
kerja = input ("masukkan pekerjaan = ")
if hutang >= 5000000 and kerja == "pns":
    bungaperbulan = 10/100 + 5/100 * hutang * 12
    print ("bunga per bulan : Rp. " , bungaperbulan)
    total_hutang = bungaperbulan * 12
    print ("total hutang : Rp. " , total_hutang)
elif hutang < 5000000 and kerja == "pns":
    bungaperbulan = 5/100 + 5/100 * hutang * 12
    print ("bunga per bulan : Rp. " , bungaperbulan)
    total_hutang = bungaperbulan * 12
    print ("total hutang : Rp. " , total_hutang)

