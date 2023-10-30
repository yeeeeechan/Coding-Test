# 1463. 1로 만들기 (진행 중)
from numpy import append
n = int(input()) - 1

while n == 0:
    if n % 3 == 0:
        n = n / 3
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n-1

# 10871. X보다 작은 수
n, x = map(int, input().split())
a = list(map(int, input().split()))
arr = []

for i in range(n):
    if a[i] < x:
        arr.append(a[i])
    else:
        continue

print(*arr)

# 10171. 고양이
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
