# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22  
#     if gender == "여자":
#         return height*height*21
#     else: print("값이 잘못되었습니다.")

# height = 166
# gender = "여자"
# weight = round(std_weight(height / 100, gender), 2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50}
for subject, score in scores.items():
    print(subject, score)

starbucks = ["동동", "딩딩", "댕댕"]
for customer in starbucks: # starbucks 안에 있는 요소 하나하나를 customer에 할당
    print("{0} 님, 커피가 준비되었습니다.".format(customer))
  