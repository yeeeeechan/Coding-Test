# a = "Is coding fun?"
# print(a.split())

# a, b = map(int, input().split())
# print(a + b)

# a, b = map(int, input().split())
# print(a+b)

# 2588번

# 1. 세 자리 자연수(1)를 입력받음
Num1 = map(int, input())

# 2. 세 자리 자연수(2)를 입력받음
Num2 = map(int, input())

# 3. 자연수(2)의 일의 자리 수를 구하고, 그걸 자연수(1)에 곱함
N1 = (Num2 % 10) * Num1
print(N1)

# 4. 자연수(2)의 십의 자리 수를 구하고, 그걸 자연수(1)에 곱함, 여기에 10을 곱함
N10 = (Num2 % 100 // 10) * Num1
print(N10)

# 5. 자연수(3)의 백의 자리 수를 구하고, 그걸 자연수(1)에 곱함, 여기에 100을 곱함
N100 = (Num2 // 100) * Num1
print(N100)

# 6. 3,4,5 결과를 더함
print(N1 + N10*10 + N100*100)

N1 = (472 % 10) * 385
print(N1)

N10 = (472 % 100 // 10) * 385
print(N10)

N100 = (472 // 100) * 385
print(N100)

print(N1+(N10*10)+(N100*100))


# R2
R1, S = map(int,input().split())
print(2*S-R1)

# 초콜릿 자르기
N, M = map(int, input().split())
print(N*M-1)

# A+B-7
range 함수 사용할 것
t = int(input())
for i in range(1, t+1):
  a, b = map(int, input().split())
  print(f'Case #{i}: {a+b}')

# A+B-8
t = int(input())
for i in range(1, t+1):
  a, b = map(int, input().split())
  print(f'Case #{i}: {a} + {b} = {a+b}')

# 오늘 날짜
import datetime
print(datetime.date.today())

# 등록
print('14')
print('dpdpdpcks')

# 오븐 시계

#시작 시각과 필요한 시간이 분단위로 주어졌을 때, 조리가 끝나는 시간을 구할 것.
# 시작하는 시각에 요리 시간을 더한다.
# 단, 시는 0~23까지 정수, 분은 0~59까지의 정수. 23시 59분에서 1분이 지나면 0시 0분이 됨

a, b = map(int, input().split())
c = int(input())

# b에 c를 더한다.
# b+c 값을 60으로 나눴을 때 몫만큼을 a에 더한다. 그리고 나머지 값도 함께 출력한다.

a = 23
b = 30
c = 30

if b+c>60 and a + int((b+c)/60) > 23 :
  print((a + int((b+c)/60))-24, (b+c)%60)
elif b+c>60 and a + int((b+c)/60) <= 23 :
  print(a + int((b+c)/60), (b+c)%60)
elif b+c==60 and a == 23:
  print(0, 0)
elif b+c==60 and a < 23:
  print(a+1, 0)
else :
  print(a, b+c)

# 풀이.... 조건식을 짜지 않고 한 줄로 계산할 수 있는 방법도 있다! >  (앞서 짠 코드는 60분이 되었을 때를 커버할 수 없어서 조건문을 죄다 넣어야 함.. 번거로움)
# 시간*60, 분, 초/60

# print(((60*A+B+C)//60)%24, (60*A+B+C)%60)
# 이런 풀이가 있었다...

# 인공지능 시계
#첫줄에 현재 시각 a, b, c가 주어지고, 다음 줄에 요리 시간 d가 초단위로 주어진다.

# 시간 입력받기
a, b, c = map(int, input().split())
d = int(input())

# 현재 시각을 초 단위로 바꾸고, d와 더해서 다시 시간 단위로 바꾼다.
# 1시간 = 60분 = 3600초 : a*3600, b*60, c

a = 23
b = 48
c = 59
d = 2515

t = int(a*3600 + b*60 + c + d)

print(t//3600%24, t//60%60, t%60)

# 저작권 (올림해서 구한 평균에서 그전 수를 구하는 문제... 예시 보고 끼워맞췄으나 제대로 이해는 안 됨.)
a, i = map(int, input().split())
print(a*(i-1)+1)