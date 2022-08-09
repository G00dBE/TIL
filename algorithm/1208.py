#count_num = int(input())



def dumping(count_num):
    breaker = True
    if 1 <= count_num <= 1000:
        input_list = list(map(int, input().split()))
        if len(input_list) == 100:
            if (max(input_list) <= 100) and (1 <= min(input_list)):
                while count_num>0 and breaker:
                    if (max(input_list) - min(input_list))>1: 
                        max_element = max(input_list)
                        min_element = min(input_list) 
                        input_list.remove(max(input_list))
                        input_list.append(max_element-1)
                        input_list.remove(min(input_list))
                        input_list.append(min_element+1)
                        count_num -= 1
                    elif (max(input_list) - min(input_list))<=1:
                        breaker = False
                        return_value = max(input_list)-min(input_list)
                        return return_value
                return_value = max(input_list)-min(input_list)
                return return_value
            else:
                return "상자높이는 1이상 100이하 입니다."        
        else:
            return "100개만 입력가능합니다."                    
    else:
        return "덤프횟수는 1이상 1000이하입니다."     
   

for j in range(10):
    print(f"#{j+1} {dumping(int(input()))}")   
        
                
    
