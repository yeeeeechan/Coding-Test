# 5355. 화성 수학
# 소수점 둘째 자리까지 출력하는 round(실수, 2)

@ = ?*3
% = ?+5
# = ?-7

t = input()
a, b, c, d = map(list, input().split)

A = float(a[0])

def functionB () :
  if b[0] == '@':
    result = A*3
  elif b[0] == '%':
    result = A+5
  else :
    result = A-7

  print(result)

def functionC () :
  if c[0] == '@':
    result = A*3
  elif c[0] == '%':
    result = A+5
  else :
    result = A-7

  print(result)

def functionD () :
  if d[0] == '@':
    result = A*3
  elif d[0] == '%':
    result = A+5
  else :
    result = A-7

  print(result)

A = 3
B = @
C = %

functionB ()
functionC ()
functionD ()

# 좀 더 간단하게. calc 함수를 사용해서. 연산자의 개수에 따라 경우를 나누지 않아도 되도록
# for i in x[1:]:
# 리스트의 길이에 따라 for문을 돌리는 횟수를 정하고 싶다면, for i in range(len(x)-1):

# print("{:.2f}".format(ans))
# 원하는 포맷에 맞게 출력하기 :  출력할 소수점 이하 자리수를 지정할 때는 .자리수f 표현으로 지정한다.

# for _ in range(n): -> 변수 _가 0,1,2,3...n의 값을 갖고 반복을 수행한다.

n = int(input())

for _ in range(n):
  line = list(map(str, input().split()))
  ans = line[0]
  for i in range(len(line)):
    if i == 0:
      ans = float(line[i])
    elif line[i] == '@':
      ans *= 3
    elif line[i] == '%':
      ans += 5
    elif line[i] == '#':
      ans -= 7

  print("{:.2f}".format(ans))


# 문자열 반복
n = int(input())

for _ in range(n): # 입력받은 테스트 케이스의 수만큼 for문을 반복한다.
  cnt, word = input().split()
  for p in word:
    print(p*int(cnt), end='') # end='' 문자열을 오른쪽으로 붙이며 출력
  print() # for p in word 출력문이 종료되면 줄넘김


# 소음
a = int(input())
b = str(input())
c = int(input())

if b == '*':
  result = a*c
elif b == '+':
  result = a+c
print(result)


# 시험 성적
score = int(input())

if score >= 90:
  print('A')
elif 80 <= score < 90:
  print('B')
elif 70 <= score <80:
  print('C')
elif 60 <= score < 70:
  print('D')
else :
  print('F')


# 세 수 --> 최소값과 최대값을 뺀 나머지를 출력
numbers = list(map(int, input().split()))

numbers.remove(min(numbers))
numbers.remove(max(numbers))

print(numbers)


# 소인수분해
n = int(input())

if n == 1:
  print('') 

for i in range(2, n+1):
  while n % i == 0:
    print(i)
    n = n/i