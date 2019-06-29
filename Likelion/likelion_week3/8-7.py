put = input('input: ')
put_list = put.split(' ')



row = int(put_list[0])
col = int(put_list[1])

line = ''

for i in range(0, row) :
    for j in range(0, col) :
        if (i+j)%2 == 0 :
            line = line + '. '
        else :
            line = line + '* '
    line = ''

