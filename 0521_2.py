#함수
def open_account():
    print("새로운 계좌가 생성됐습니다")

open_account()

def deposit(balance,money):
    print("입금완료. 잔액 : {}원".format(balance+money))
    return balance + money

balance = 0
balance = deposit(balance, 10000)
print(balance)
