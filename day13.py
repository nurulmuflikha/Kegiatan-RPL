#day13
#RPL
#belajar perulangan while

while True:

 user = input ("apakah pengguna menyukai bubur ayam =")
 user = user.lower()
 if user == "ya":
    user = input ("kamu suka bubur yang diaduk atau tidak?")
    user = user.lower()
    if user == "diaduk":
       print ("beh kalau di aduk buburnya jadi mirip?")
    else:
       print ("anda ternyata manusia beradab") 
 else: 
     print ("cobain lagi deh kapan-kapan, sehat dan bergizi, siapa tau jadi suka")
     break
