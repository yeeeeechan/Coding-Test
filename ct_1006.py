# Hunt the Rabbit (13777)
# 이진 탐색 문제
# median_low를 이용해 중위값을 반복하여 찾는 것인 줄 알았으나 binary_search라는 알고리즘이 있었다...
# 배열 전체의 중간값을 target 값과 비교
# 중간값이 target 값보다 크면 왼쪽 부분만 선택
# 왼쪽 부분의 중간값을 다시 target 과 비교


# import statistics as st

# r = int(input())
# cards = list(range(1,50))

# if r == 25 :
#   print(25)

# while r != 0 :
#   if r < 25 :
#     result = st.median_low(cards[:25])
#     print(int(result))
#   elif r < 13 :
#     result = st.median_low(cards[:13])
#     print(int(result))
#   elif r < 7 :
#     result = st.median_low(cards[:7])
#     print(int(result))
#   elif r < 4 :
#     result = st.median_low(cards[:4])
#     print(int(result))
#   elif r < 2 :
#     result = st.median_low(cards[:2])
#     print(int(result))
#   elif r > 25 :
#     result = st.median_low(cards[25:])
#   print(int(result))
#   if r == result :
#     break

# target = int(input())
# # arr = list(range(1, 50))
# start = 1
# end = 50

# def binary_search (arr, target, start, end):
#   while True:
#     if target == 0:
#       break
#     while start <= end:
#       mid = (start + end) // 2
#       print(mid, end='')
#       if arr[mid] == target:
#         return mid
#       elif arr[mid] > target:
#         end = mid - 1
#       else:
#         start = mid + 1
#     print(sep='/n')

#%%

while True:
    start, end = 1, 50
    target = int(input())
    if target == 0:
        break
    while True:
    	# start와 end의 중간을 구한다
        mid = (start + end) // 2
        # 중간을 프린트
        print(mid, end=' ')
        # n과  N이 동일해지면 반복 끝낸다
        if mid == target:
            break
        # 중간 수보다 작다면 end를 줄인다
        elif mid > target:
            end = mid - 1
        # 중간수 보다 크다면 start를 늘린다
        else:
            start = mid + 1
    # 반복이 끝나면 출력 줄을 바꾼다.
    print(sep = '\n')

    #%%

# 거스름돈(5585)
# n원의 물건을 사고 1000원을 냈을 때, 가장 적게 잔돈을 주는 개수를 구하라 (잔돈은 500, 100, 50, 10, 5, 1)

price = int(input())

def cal_change (price):
  change = 1000 - price
  
  a = change // 500
  b = (change % 500) // 100
  c = (change % 100) // 50
  d = (change % 50) // 10
  e = (change % 10) // 5
  f = (change % 5) // 1

  return a+b+c+d+e+f

print(cal_change(price))


# N번째 큰 수(2693)
# 배열에서 세 번째 큰 수를 출력하기( > 오름차순 정렬해서 인덱스 8 값 출력하면 되지 않을까?)

# 배열을 입력받는 코드
n = int(input())

for i in range(n): # 입력받은 테스트 케이스만큼 for문을 반복한다.
  arr = list(map(int, input().split()))
  arr.sort()
  print(arr[-3])