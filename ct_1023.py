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
