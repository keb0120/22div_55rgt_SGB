##문자열
a = "970120-1234567"
print(a[0]) # a의 1자리 문자열
print(a[0:2]) #a의 0부터 2직전까지 (0,1)
print(a[:6]) # 처음부터 6직전까지
print(a[7:]) # 7부터 마지막까지
print(a[-7:]) # 맨뒤에서 7번째부터 끝까지

##문자열
python = "Python is Amazing"
print(python.lower()) # 소문자화
print(python.upper()) # 대문자화
print(python[0].isupper()) # 0의자리 문자가 대문자인지 => true or false
print(len(python)) # 길이
print(python.replace("Python", "java")) # python 을 java 로 replace (교체)

index = python.index("n") #n이 몇번째 순서(index)에 있는지
print(index)
index = python.index("n",index+1) # 두번째 n의 index 를 찾는법
print(index)

print(python.find("java")) # java 찾기 결과 : -1 / 1
#print(python.index("java")) # java가 없어서 오류
print(python.count("n")) # n 갯수찾기

##문자열 포맷
print("a" + "b")
print("a","b") # 띄어쓰기가 자동

print("나는 %d살입니다" % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요" % "A")
print("나는 %s살입니다 " %20 )
print("나는 %s와 %s을 좋아해요." % ("파랑","빨강") )
print("나는 {}살입니다.".format(20))
print("나는 {},{} 좋아해요.".format("ㅁ","ㅂ"))
print("{0},{1}".format("a","b"))
print("{1},{0}".format("a","b"))
print("{age},{color}".format(age =20,color="red"))
print("{age},{color}".format(color="red",age =20,))
#방법 4 (v3.6 over)
age= 20
color= "red"
print(f"나는 {age},{color}") # f는ㅁ ㅓ임?

## 탈출 문자



      
