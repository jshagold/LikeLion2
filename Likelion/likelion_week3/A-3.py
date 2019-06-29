put = input()


dic = {}
for i in range(0, int(put)) :
    a = input()
    line = a.split(' ')
    if line[0] in dic :
        dic[line[0]] = dic[line[0]]+int(line[1])
    else :
        dic[line[0]] = int(line[1])

a = dic.items()
b = list(a)
result = sorted(b)
for i in range(0, len(b)) :
    print(result[i][0]+' '+str(result[i][1]))



