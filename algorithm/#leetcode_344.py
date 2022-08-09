# leetcode 344
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

input_string_list = input()
string_list = []
for element in input_string_list: 
    if element.isalpha():          #문자인 요소만 추출해서
        string_list += [element]   #list로 만들고
print(string_list[::-1])           #역순으로 출력