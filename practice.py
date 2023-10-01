print(2 + 3 * 4) #14
print((2 + 3 ) * 4 ) #20
number = (2 + 3 ) * 4
number += 2
print(number)

print(abs(-6)) #절댓값
print(pow(4, 2)) #4의 2승
print(max(5, 12)) #두 인수 중 최대값
print(min(5, 12)) #두 인수 중 최소값
print(round(3.14)) #반올림
print(round(3.99))

#문자열 출력하기
age = 30
color = "빨간"
print(f"나는 {age}살이고, {color}색을 좋아해.")

#---탈출 문자---
# \n : 줄바꿈 
# \ : 따옴표 앞에 써주면 그대로 출력
# \\ : 문장 내에서 \로 출력
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #Red Apple을 적고 난 뒤에 앞으로 커서를 옮겨서 Pine을 적음

# \b : 백스페이스 (한 글자 삭제)
# \t : 탭