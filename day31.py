#day31
#contoh kasus baru menggunakan nested if
#menghitung gaji karyawan

golongan = int (input ("masukkan golongan = "))
tahun_masuk_kerja = int (input("masukkan tahun masuk kerja = "))
tahun_skrg = 2011
total_masa_kerja = 2011 - tahun_masuk_kerja

if total_masa_kerja >= 7 :
    bonus = 150000
    if golongan == 1 :
        gaji_pokok = 1500000
    elif golongan == 2 :
        gaji_pokok = 1200000
    elif golongan == 3 :
        gaji_pokok = 1000000
        
elif total_masa_kerja < 7 :
    bonus = 0
    if golongan == 1 :
        gaji_pokok = 1500000
    elif golongan == 2 :
        gaji_pokok = 1200000
    elif golongan == 3 :
        gaji_pokok = 1000000
        
gaji_keseluruhan = gaji_pokok + bonus
print (f"gaji pokok = Rp. {gaji_pokok}")
print (f"bonus = {bonus}")
print (f"masa kerja karyawan = {total_masa_kerja} tahun lamanya")
print (f"gaji keseluruhannya = Rp. {gaji_keseluruhan}")

#
