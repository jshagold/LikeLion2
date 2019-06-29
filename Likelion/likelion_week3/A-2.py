put = input()

matrix = []

for i in range(0, int(put)) :
    line = input()
    m_l = line.split(' ')
    matrix.append(m_l)

key = input()


for i in range(0, len(matrix)) :
    for j in range(0,len(matrix[i])) :
        if key == matrix[i][j] :
            if j == 0 :
                print(matrix[i][1])
            else :
                print(matrix[i][0])

