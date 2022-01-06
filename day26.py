hutang = int (input ("masukkan hutang = Rp. "))
kerja = input ("masukkan pekerjaan = ")
if kerja == "pns" :
    if hutang >= 5000000 and kerja == "pns":
        print ("pajak 15% karna pns")
        bungaperbulan = 10/100 + 5/100 * hutang * 12
        print ("bunga per bulan : Rp. " , bungaperbulan)
        total_hutang = bungaperbulan * 12
        print ("total hutang : Rp. " , total_hutang)
        print ("pajak 15% karna pns")
    elif hutang < 5000000 and kerja == "pns":
        print ("pajak 10% karna pns")
        bungaperbulan = 5/100 + 5/100* hutang * 12
        print ("bunga per bulan : Rp. " , bungaperbulan)
        total_hutang = bungaperbulan * 12
        print ("total hutang : Rp. " , total_hutang)
else:
    if hutang >= 5000000:
        bungaperbulan = 10/100 * hutang * 12
        print ("bunga per bulan : Rp. " , bungaperbulan)
        total_hutang = bungaperbulan * 12
        print ("total hutang : Rp. " , total_hutang)
        print ("pajak tetap 10% karna bukan pns")
    elif hutang < 5000000:
        bungaperbulan = 5/100 * hutang * 12
        print ("bunga per bulan : Rp. " , bungaperbulan)
        total_hutang = bungaperbulan * 12
        print ("total hutang : Rp. " , total_hutang)
        print ("pajak tetap 5% karna bukan pns")
