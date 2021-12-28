#day17
#RPL
#belajar fungsi rekursif

def pantulanCermin (batas, i = 1):
    if (i < batas):
        pantulanCermin (batas , i + 1)
        print (f'pantulan cermin ke {i}')
pantulanCermin (10)
