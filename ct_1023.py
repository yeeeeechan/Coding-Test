# 5086. 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")

# 5717. 상근이의 친구들
while True:
    f1, f2 = map(int, input().split())
    if f1 == 0 and f2 == 0:
        break

    print(f1+f2)

# 9610. 사분면
dots = int(input())
result1 = 0
result2 = 0
result3 = 0
result4 = 0
result5 = 0

for i in range(dots):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        result1 += 1
    elif x < 0 and y > 0:
        result2 += 1
    elif x < 0 and y < 0:
        result3 += 1
    elif x > 0 and y < 0:
        result4 += 1
    elif x == 0 or y == 0:
        result5 += 1

print("Q1:", result1)
print("Q2:", result2)
print("Q3:", result3)
print("Q4:", result4)
print("AXIS:", result5)

# 8958. OX 퀴즈
case = int(input())

for _ in range(case):
    list = list(input())
    score = 0
    sum_score = 0

    for ox in list:
        if ox == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

# 9506. 약수들의 합
while True:
    n = int(input())
    if n == -1:
        break
    else:
        result = []
        total = 0
        for i in range(1, n//2+1):
            if n % i == 0:
                result.append(i)
                total += i
        if n == total:
            print(n, "=", end=" ")
            print(*result, sep=" + ")
        else:
            print(n, "is NOT perfect.")

# 10162. 전자레인지
t = int(input())

if t % 10 != 0:
    print('-1')
else:
    a, b, c = 0, 0, 0

    a = t // 300
    b = (t % 300) // 60
    c = (t % 60) // 10
    print(a, b, c)

# 10103. 주사위 게임
round = int(input())
p1, p2 = 100, 100

for i in range(round):
    a, b = map(int, input().split())

    if a == b:
        continue
    elif a > b:
        p2 -= a
    elif a < b:
        p1 -= b

print(p1)
print(p2)

# 10214. Baseball
c = int(input())

for i in range(c):
    y_score = 0
    k_score = 0

    for _ in range(9):
        y, k = map(int, input().split())
        y_score += y
        k_score += k

    if y_score > k_score:
        print("Yonsei")
    elif y_score < k_score:
        print("Korea")
    else:
        print("Draw")

# 11557. Yangjojang of The Year
# sch_name, max라는 변수를 초기화해 선언해 주고,
# 두 번째 for문이 반복될 때마다 drink를 정수형으로 저장하여 max보다 클 때 max에 할당하는 식으로 값을 비교함
c = int(input())

for i in range(c):
    sch_name = ''
    max = 0
    s = int(input())

    for _ in range(s):
        sch, drink = input().split()
        drink = int(drink)
        if drink > max:
            sch_name = sch
            max = drink
    print(sch_name)

# 10757. 큰 수 A+B
# import sys
# input = sys.stdin.readline # 입력받는 양이 많을 때 속도를 단축할 수 있다! (이 문제에서는 별반 차이 없음)

a, b = map(int, input().split())
print(a+b)
