#SWEA 4828
# min max
def max(num_list):           # max 함수
    max_number = num_list[0]
    for number in num_list:
        if max_number < number:
            max_number = number
    return max_number

def min(num_list):          # min 함수 
    min_number = num_list[0]
    for number in num_list:
        if min_number > number:
            min_number = number
    return min_number

for i in range(int(input())):  
    input_testcase = int(input())
    input_list = list(map(int,input().split()))
    print(f'#{i+1} {max(input_list)-min(input_list)}') # 최대값 - 최솟값