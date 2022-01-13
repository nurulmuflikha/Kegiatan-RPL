#day33

#belajar matrix

print ("mengakses elemen matrix")

matrix = [[3,6] ,
        [2,4]]

for x in range (0 , len(matrix)):
    for y in range (0 , len(matrix[0])):
        print (matrix[x], end=' '),
    print (matrix[y])

#menggunakan parameter end=' ' pada print guna utk menyerupai matrix


print ("penjumlahan 2 matrix")

mat1 = [[3,4],
        [1,2]]

mat2 = [[2,4],
        [1,3]]

result = []
for n in range (len(mat1)):
    row = []
    for m in range (len(mat1[n])):
        row.append(mat1[n][m] + mat2[n][m])
    result.append(row)
    
for row in result:
    print (row)
