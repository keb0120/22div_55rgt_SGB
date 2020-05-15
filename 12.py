'''
#줄바꿈
# \" , \' : 문장 내 따옴표

#print("저는 "a"입니다.")
print("저는 'a'입니다.")
print('저는 "ㅁ"입니다.')
print("저는 \"a\"dlqsle.")

# \\ : 문장내에서 \
#print("C:\users")
print("C:\\users")

# \r : 커서를 맨앞으로
print("Red Apple\r a") # 원래는 됨

# \b: 백스페이스 (한글자삭제)
print("Redd\bApple") # ㅇㅒ도 원래는ㄷ ㅚㅁ

# \t : 탭

quiz ) 사이트별로 비밀번호를 만들어주는 프로그램
ex) http://naver.com
규칙1: http:// 부분제외 -> naver.com
2 : 처음만나는 . 이후 부분은 제외 -> naver
3 : 남은 글자 중 처음 세자리 nav + 글자갯수 5 + 글자 내 e 갯수 1 + ! 로 구성

# 리스트 []
sub = ['a','b','c']
print(sub)
# 몇번쨰인지 찾는법
print(sub.index('b'))
#리스트 추가
sub.append('d')
print(sub)
#사이에 추가
sub.insert(1,'aa')
print(sub)
#리스트 뒤에서부터 제거
print(sub.pop())
print(sub)
#같은 문자 갯수 찾기
sub.append('a')
print(sub)
print(sub.count('a'))
#정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
#뒤집기
num_list.reverse()
print(num_list)
#다 지우기
num_list.clear()
print(num_list)
#다양한 자료형
num_list = [1,2,3,4,5]
mix_list = ["a",1,True]
print(mix_list)
#리스트 확장
num_list.extend(mix_list)
print(num_list)
'''

####사전
cabinet = {3:"A",100:"B"}

print(cabinet[3])
