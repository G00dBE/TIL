input_string = input()    
string_list = []
for string in input_string:  
    if string.isalpha():     #입력받은 문자열 중 문자만 추출
        string_list += [string.lower()]  # 소문자로 통일
if string_list == string_list[::-1]:     # 문자 역순과 동일여부 체크
    print("true")
else:
    print("false")       
        