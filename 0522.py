'''#함수
def open_account():
    print("새로운 계좌가 생성됐습니다")

open_account()

def deposit(balance,money):
    print("입금완료. 잔액 : {}원".format(balance+money))
    return balance + money

balance = 0
balance = deposit(balance, 10000)
print(balance)
'''
'''def withdraw(balance,money,time):
    commission = 100
    if balance >=money:
        if time >=18:
            print("출금이 완료 됐습니다. 잔액은 {0}입니다.".format(balance-money-commission))
            return commission,balance -money-100
        else:
            print("출금이 완료 됐습니다. 잔액은 {0}입니다.".format(balance-money))
            return balance -money
    else:
        print("잔액이 부족합니다.")
        return balance

balance =1000
commission,balance = withdraw(balance,50,19)
print(f"수수료{commission},잔액{balance}")'''
'''
#기본값
def profile(name, age=20,main_lang="python"):
    print(f"이름={name}\t 나이={age}\t 주언어={main_lang}")

profile("응점잉")
profile("응점잉",25,"c")
'''
'''
def profile(name, age=20,main_lang="python"):
    print(f"이름={name}\t 나이={age}\t 주언어={main_lang}")
    
#키워드값
profile(name="응점잉",main_lang="java",age=222)
'''
#가변인자
'''def profile(name, age,lang1,lang2,lang3,lang4,lang5):
    print(f"이름={name}\t 나이={age}\t,",end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

 '''   '''
def profile(name, age,*lang):
    print(f"이름={name}\t 나이={age}\t,",end=" ")
    for i in lang:
        print(i,end=" " )
    print()
profile("응저밍",33,"python","java","c","c++","C#")
profile("응저밍2",25,"a","b")
'''
'''
#지역변수 / 전역변수
gun = 10
def checkpoint(soldiers): # global (전역변수 사용하는) 방식은 코드관리에 비효율
    global gun # 전역공간에 있는 gun 을 사용
    gun = gun - soldiers
    print("[함수 내] 남은총 : {}".format(gun))
def checkpoint_ret(gun ,soldiers): ## 이 방식이 더 효율적
    gun -= soldiers
    print("[함수 내] 남은총 : {}".format(gun))
    return gun


print("총:{}".format(gun))
gun = checkpoint_ret(gun,2)
print("총:{}".format(gun))
'''
#표준입출력
print("a","b","c" , sep= ",",end =" ")
print("힝")
import sys
print("a","b","c" , file=sys.stderr) #에러글씨 (빨간글씨)
print("a","b","c" , file=sys.stdout)

score ={ "수학":0,"영어":50,"코딩":100}
for subject, score in score.items():
    print(subject.ljust(10),str(score).rjust(5),sep=":")#ljust , rjust ==> 총 x칸의 공간 중에 좌/우로 정렬

for num in range(1,21):
    print("대기번호 : ",str(num).zfill(3)) # 3자리수중에 남는 공간은 zero 로 fill

answer = input("애니띵 : ")
print(answer)
