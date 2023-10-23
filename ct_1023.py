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
