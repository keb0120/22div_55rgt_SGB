'''weather = input("날씨는?")
if weather == "비"or"눈":
    print("비가 옴")
elif weather == "미세먼지":
    print("미세먼지 ㅇㅇ")
else:
    print("개좋음")


temp = int(input("기온은?"))
if temp>=30:
    print("더움")
elif temp>=10 and temp<30:
    print("낫밷")
elif temp>=0 and temp<10:
    print("아우터")
else:
    print("추웡ㅇ")
'''
'''
for num in range(1,6):
    print("대기번호 : {0}".format(num))

people=["A","B","C"]
for customers in people:
    print("{}가 입장하셨습니다".format(customers))
'''
'''
customers = " A"
i = 5
while i >=1:
    print("{0}, 준비완료. {1} 번 남았습니다.".format(customers,i))
    i -= 1
    if i==0:
        print("폐기완료")

customers = "A"
person = "Unknown"

while person != customers:
    print("A의 커피가 나왔습니다")
    person = input("이름은?")
    if person!=customers:
        print("주인이 아닙니다")
        '''
'''
absent = [2,5]
nobook= [7]
for student in range(1,11):
    if student in absent:
        print("결석입니다")
        continue
    elif student in nobook:
        print("수업끝")
        break
    print("{}".format(student))
'''
'''
# 1,2,3,4 -> 101,102,103,104
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

students = ["Iron man","Thor"]
students = [len(i) for i in students]
print(students)
'''


