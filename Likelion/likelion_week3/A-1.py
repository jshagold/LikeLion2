b_input_list = input()

input_list = b_input_list.split(' ')

count = 0
for i in range(0, len(input_list)):
    for j in range(0, i) :
        if input_list[j] == input_list[i] :
            count = count + 1
    print(count)
    count = 0
