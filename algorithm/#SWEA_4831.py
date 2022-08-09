#SWEA_4831

def charge_bus(idx, battery, bus_stop_list):    #충전소를 반환하는 함수
    charge_station = 0
    for i in range(battery,0,-1):               # 가장 멀리갈 수 있는 정류소부터 순회
        if bus_stop_list[idx+i] == 1:           # 충전 최대이동 거리 중에 충전소 유무 찾기
            charge_station = idx+i              # 충전소를 찾으면 시작점을 출발인덱스+충전소까지 거리
            break
        else:
            continue
    return charge_station                       # 새로운 출발지점
        
T = int(input())
for i in range(T):
    battery, bus_stop, charge = map(int,input().split())   #충전최대 이동거리, 총 정류장 수, 충전소 개수
    bus_stop_list = [0]*(bus_stop+1)                       #출발지 0 추가
    charge_list = list(map(int,input().split()))           #충전소 위치를 리스트로 반환
    for charge_station in charge_list:
        bus_stop_list[charge_station] = 1                  #충전소가 있는 곳은 1로 나타낸 리스트
    start = 0                                              #출발지 0으로 초기화
    count_charge = 0                                       #총 충전횟수
    while start+battery < bus_stop:                        
        station = charge_bus(start, battery, bus_stop_list)  # 충전하게 되는 정류장
        if station != 0:                                       
            start = station        # 충전한 정류장을 기준으로 출발지점 갱신
            count_charge += 1    
        else:                      # 충전을 못하면 station == 0
            print(f'#{i+1} {0}')   # 앞에 얼마나 충전했든, 종점까지 도착불가
            break    
    if start+battery >= bus_stop:
        print(f'#{i+1} {count_charge}')        