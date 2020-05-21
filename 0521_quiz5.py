from random import *

count =0

for i in range (1,51):
    time = randrange(5,51)
    if time >5 and time <15:
        print("[0] {}번째 손님(소요시간 : {}분)".format(i,time))
        count +=1
    else:
        print("[ ] {}번째 손님(소요시간 : {}분)".format(i,time))

        
print ("총 탑승 승객 : {}분".format(count))
