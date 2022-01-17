#tipe data set
#set menambah anggota baru
himpunan_manusia = {'mikha' , 'parif' , 'arman'}
print(himpunan_manusia)

# menambah satu-satu
himpunan_manusia.add('gibran')
himpunan_manusia.add('merry')

# menambah lebih dari satu anggota sekaligus
himpunan_manusia.update({ 'naya' , 'hendra' , 'rasul'})
# bisa juga pakai list
himpunan_manusia.update(['heri', 'zahra'])

print(himpunan_manusia)