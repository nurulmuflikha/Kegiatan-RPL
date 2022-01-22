# Menginput Nilai Variabel
# Membuat Variabel tukar dan Menukar nilai Variabel lain
x = input('Tuliskan nilai x: ')
y = input('Tuliskan nilai y: ')

tukar = x
x = y
y = tukar
print('Nilai x Setelah Ditukar adalah: {}'.format(x))
print('Nilai y Setelah Ditukar adalah: {}'.format(y))