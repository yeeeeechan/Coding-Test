# 화성 수학
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
# 리스트의 길이에 따라 for문을 돌리는 횟수를 정하고 싶다면, for i ing range(len(x)-1):

# 문자열 반복

s = input()