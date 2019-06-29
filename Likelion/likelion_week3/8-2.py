first = input()

a = first.split(' ')
row = int(a[0])
column = int(a[1])
matrix = []

for i in range(0, row) :
    i_row = input()
    a = i_row.split(' ')
    matrix.append(a)

cmp = int(matrix[0][0])
f_row = 0
f_col = 0


for i in range(0,row) :
    for j in range(0,column) :

        if(int(matrix[i][j]) > int(cmp)) :
            cmp = matrix[i][j]
            f_row = i
            f_col = j
print(str(f_row)+' '+str(f_col))






