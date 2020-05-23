'''#10자리 중에 >로 오른쪽정렬
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#좌정렬 빈칸 _
print("{0:_<10}".format(500))
#3자리마다 콤마 찍기
print("{0:,}".format(10000000))

print("{0:^<+30,}".format(1000000000000))
#소수점
print("{0:f}".format(5/3))
#소수점 특정자리수
print("{0:.2f}".format(5/31))

'''
#파일입출력
'''
score_file = open("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 0", file=score_file)
print("영어 : 0", file=score_file)
score_file.close()
'''
'''
score_file=open("score.txt","a",encoding="utf8") # a = append : 내용추가
score_file.write("과학 : 22") #write 메소드 사용하면 자동 줄넘김 x
score_file.write("과학 : 22")
score_file.close()
'''
#score_file = open("score.txt","r",encoding="utf8") # r = read
'''
#print(score_file.read())

#한줄씩 가져오기
print(score_file.readline()) # 줄별로 읽기 , 한줄 읽고 커서는 다음줄
print(score_file.readline(),end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()
'''
#몇줄인지 모를때
'''while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
'''
'''
#score_file.close()
#리스트에 넣어서 처리
lines = score_file.readlines() # list 형태로 모든 라인을 저장
for line in lines:
    print(line, end="")
score_file.close()
'''

#pickle
'''
import pickle

profile_file = open("profile.pickle","wb") #b = binary pickle에서 필수 encoding은 안해도됨\
profile = {"이름":"ㅁ","나이":30,"취미":["ㅁ","ㄴ","ㅇ"]}
pickle.dump(profile,profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile= pickle.load(profile_file)
print(profile)
profile_file.close()
'''

#with
'''
import pickle
with open("profile.pickle","rb") as profile_file: # close 피료 x
    print(pickle.load(profile_file))
'''
'''
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("공부중")

'''
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
