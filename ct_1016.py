# 2476. 주사위 게임
p = int(input())
results = []

for i in range(p) :
  a, b, c = sorted(map(int, input().split()))

  def dice(a, b, c) :
   if a == b == c:
    result1 = 10000 + a*1000
    return result1
   elif a == b != c :
    result2 = 1000 + b*100
    return result2
   elif a != b == c :
    result3 = 1000 + b*100
    return result3
   else :
    result4 = c*100
    return result4
  results.append(dice(a, b, c))

max_results = max(results)
print(int(max_results))

# 2754. 학점 계산
score = input()

if score == "A+" :
 print(4.3)
elif score == "A0" :
 print(4.0)
elif score == "A-" :
 print(3.7)
elif score == "B+" :
 print(3.3)
elif score == "B0" :
 print(3.0)
elif score == "B-" :
 print(2.7)
elif score == "C+" :
 print(2.3)
elif score == "C0" :
 print(2.0)
elif score == "C-" :
 print(1.7)
elif score == "D+" :
 print(1.3)
elif score == "D0" :
 print(1.0)
elif score == "D-" :
 print(0.7)
elif score == "F" :
 print(0.0)

# 2884. 알람 시간
h, m = map(int, input().split())

alarm = h * 60 + m - 45
aH = alarm // 60
aM = alarm % 60

if h == 0 and m < 45 :
  aH = 23
elif aH == 24:
  aH = 0

print(aH, aM)

# 7567. 그릇
plates = input()
plate = 10

for i in range(1, len(plates)):
 if plates[i] == plates[i-1]:
    plate += 5
 else :
    plate += 10
print(plate)

# 5063. TGN
t = int(input())

for i in range(t) :
 n, y, cost = map(int, input().split())
 
 yes_ad = y - cost

 if n > yes_ad :
    print("do not advertise")
 elif n < yes_ad :
    print("advertise") 
 else :
    print("does not matter")

# 10102. 개표
vc = int(input())
v = input()

A_score = 0
B_score = 0

for i in range (vc) :
  if v[i] == "A" :
   A_score += 1
  else :
   B_score += 1
  
if A_score > B_score :
   print("A")
elif A_score < B_score :
   print("B")
else :
   print("Tie")