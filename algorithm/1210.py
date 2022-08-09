def find_ladder(list_array):
    initial_position = [0,0]
    for i in range(len(list_array)-1):
        for j in range(len(list_array)-1):
            if list_array[i+1][j] == 1:
                initial_position[0] = i+1
                initial_position[1] = j
            elif list_array[i][j+1] == 1:
                initial_position[0] = i
                initial_position[1] = j+1
                
    list_array[initial_position[0]][initial_position[1]]=2                        
    return initial_position[0]            



for i in range(10):
    testcase = int(input())
    list_array = []
    for j in range(100):
        list_array.append(list(map(int, input().split())))
    print(f'{testcase} {find_ladder(list_array)}')    
                       
                   