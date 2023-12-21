# 1920. 수 찾기
n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    left, right = 0, n-1
    isExist = 0

    while left <= right:
        mid = (left + right) // 2
        if i == n_list[mid]:
            isExist = 1
            print(isExist)
            break

        elif i > n_list[mid]:  # 요소가 중간값보다 크면
            left = mid + 1
            
        else:
            right = mid - 1
    if isExist == 0:
        print(isExist)
