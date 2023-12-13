# 10871. X보다 작은 수
from numpy import append
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


# 1003. 피보나치 함수 (다이나믹 프로그래밍)_출력 횟수 리스트에 대한 이해가 완벽하게 되진 않은 것 같다.
# 피보나치 수열은 f(n) = f(n-1)+f(n-2)의 형태로 이루어짐
# 숫자가 0일 때 호출되는 0은(zero[0]) 1번, 1일 땐 0번, 2일 땐 1번
# 숫자가 0일 때 호출되는 1은(one[0]) 0번, 1일 땐 1번, 2일 땐 1번
# f(2) = f(1)+f(0)

def fib(n):
    zero = [1, 0, 1]  # 0이 출력되는 횟수 리스트
    one = [0, 1, 1]  # 1이 출력되는 횟수 리스트
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i-1] + zero[i])
            one.append(one[i-1] + one[i])
    print(f'{zero[n]} {one[n]}')


t = int(input())
for _ in range(t):
    n = int(input())
    fib(n)

# 1463. 1로 만들기 (진행 중)
# 다이나믹 프로그래밍은 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 의미한다.
# 이걸 위해서 앞선 연산의 결과를 저장해서 재사용하는 방식을 차용한다.
# 이 문제에선 어떻게 연산 과정을 나눠서 재사용할 수 있을까..?
n = int(input()) - 1

while n == 0:
    if n % 3 == 0:
        n = n / 3
    elif n % 2 == 0:
        n = n / 2
    else:
        n = n-1

# 10828. 스택
class Stack:
    def __init__(self, data):
        self.top = None