def sumarray(list_2):
    list_2_vertical = list(zip(*list_2))
    sum_array = []
    sum_array_vertical = []
    sum_diagonal = []
    for i in range(len(list_2)):
        sum_array.append(sum(list_2[i]))
        sum_array.append(sum(list_2_vertical[i]))
        for j in range(len(list_2)):
            if i == j:
                sum_diagonal.append(list_2[i][j]) 
            elif i+j == 99:
                sum_diagonal.append(list_2[i][j])
    sum_array.extend(sum_array_vertical)
    sum_array.extend(sum_diagonal)
    return max(sum_array)

for i in range(10):
    list_2 = []
    testcase_num = int(input())
    for j in range(100):
        list_2.append(list(map(int, input().split())))
    print(f'#{testcase_num} {sumarray(list_2)}')                
    
    