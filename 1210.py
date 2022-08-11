import sys
sys.stdin = open('input (4).txt')

def find_ladder(list_array):
    di = [0, 0, -1]
    dj = [-1, 1, 0]
    move = 0
    for k in range(len(list_array)):
        if list_array[99][k] == 2:    #도착점 위치 찾기
            nj=k             
    ni = 99          
    while ni>0:
        ni += di[move]                      # 한칸이동
        nj += dj[move]
        if (0<=ni<100) and (0<=nj<100) and (list_array[ni][nj] == 1):
            list_array[ni][nj] = 0
            ni += di[move]
            nj += dj[move]   
        elif nj>=100 or nj<0 or ni>=100 or ni<0 or list_array[ni][nj] == 0:  #인덱스 오류/0일 경우 
            ni -= di[move]       #실행취소
            nj -= dj[move]
            move = (move+1)%3    #방향전환                                      
    return nj

for i in range(10):
    tc = int(input())
    list_array = []
    for j in range(100):
        list_array.append(list(map(int, input().split())))
    print(f'#{i+1} {find_ladder(list_array)}')    
                       
                   