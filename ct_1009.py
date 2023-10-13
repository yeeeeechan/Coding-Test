# 수들의 합
# 반복문으로 자연수 1부터 1씩 증가한 값들을 더한다. 입력된 자연수n보다 합계가 작거나 같을 때 종료하고 더한 횟수를 카운트한다.

n = int(input())
count = 0
sum = 0
i = 1

while sum <= n:
  sum += i
  i += 1
  count += 1

print(count-1) # 마지막 while문이 돌아갈 때 합계가 n을 초과하게 되므로 1을 빼준다.

# 윤년
y = int(input())

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :
  print(1)
else :
  print(0)

# 평균 점수 (단, 조건부 표현식을 사용하면 더 간결하게 작성할 수 있다!)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if a < 40 :
  a = 40

if b < 40 :
  b = 40

if c < 40 :
  c = 40

if d < 40 :
  d = 40

if e < 40 :
  e = 40

average = int((a+b+c+d+e)/5)
print(average)

# 같은 문제- for문, 조건부 표현식

s = 0
for i in range(5):
  s += max(40, int(input())) # 입력받은 정수와 40 중 최대값을 반환하여 s에 더한다.
print(s/5)

s = 0
for i in range(5) :
  k = int(input())
  s += k if k >=40 else 40 # k가 40 이상이면 s에 k를 더하고, 아니면 40을 더하겠다.
print(int(s/5)) # 정수로 출력해야 하므로 int씌워서

# 최소공배수 (1934)
# 입력받은 두 수의 배수를 구한다. (한 번만 구하고 반복 중단)
# 단, 이렇게 풀면 시간 초과가 뜬다... a*b / (a,b의 최대 공약수) 로 풀어야 한다.
# 최대 공약수는 유클리드 호제법으로 구한다. (= a와 b의 최대공약수는 a%b와 b의 최대 공약수와 같다.)
# 큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다. 큰 수를 작은 수로 계속 나누어서, 나누어 떨어질 때까지 반복한다. 나누어 떨어질 때(나머지가 0일 때), 나누는 수가 최대공약수이다.
# a, b의 최대공약수는 (a-b), b의 최대공약수와 같다. -> 큰 수에서 작은 수를 뺀다. 같아질 때까지 큰 수를 작은 수만큼 줄이는 것을 반복한다. 같아지면 그 수가 최대공약수이다.

# # 이게 정석 최대공약수(gcd) 구하는 코드
# for i in range(max(a, b), a*b+1): # a와 b 중 큰 수부터 시작해 두 수를 곱한 값까지 범위를 정한다.
#   if i % a == 0 and i % b == 0:
#     print(i)
#     break

t = int(input())

def gcd (a, b) :
  if b > a :
    a, b = b, a

  while (b != 0):
    a = a % b
    a, b = b, a
  return a

def lcm (a, b):
  return (a*b)//gcd(a, b)

for _ in range(t):
  a, b = map(int, input().split())
  result = lcm (a, b)
  print(result)

# 주사위 세 개(2480)
a, b, c = map(int, input().split())

if a == b == c :
  print(10000 + a*1000)
elif a == b != c :
  print(1000 + a*100)
elif a != b == c :
  print(1000 + b*100)
elif a == c != b:
  print(1000 + a*100)
else :
  max = max(a, b, c)
  print(max*100)

# 크냐? (4101)
while True :
  a, b = map(int, input().split())
  if a == 0 and b == 0 :
    break
  if a > b :
    print('Yes')
  else :
    print('No')

# 과자 (10156)
k, n, m = map(int, input().split())
p = k*n-m

if p >= 0 :
  print(p)
elif p < 0 :
  print(0)

# 네 번째 점 (3009)
dots = []

for i in range(3):
  x, y = map(int, input().split())
  dots.append([x, y])

dots1 = [coord for point in dots for coord in point]

dotsX = dots1[0::2]
dotsY = dots1[1::2]

def unique (input_list):
  count_dict = {}
  unique_elements = []

  for item in input_list:
    if item in count_dict:
      count_dict[item] += 1
    else:
      count_dict[item] = 1
  
  for item, count in count_dict.items():
    if count == 1 :
      unique_elements.append(item)
  
  return unique_elements

x = unique(dotsX)
y = unique(dotsY)

print(x[0], y[0])

# 같은 문제 더 간단한 풀이 (count 메소드)
X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)