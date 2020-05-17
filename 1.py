from random import *

num = list(range(1,21))

print(num)

shuffle(num)
print(num)

sample1 = sample(num,1)

num = set(num)
sample1 = set(sample1)
num = num - sample1
print(num)
num = list(num)

sample2 = sample(num,3)
print("치킨 당첨자 : {}".format(sample1))
print("당첨자 :  {}".format(sample2))

#----------------------

num = list(range(1,21))

shuffle(num)
winners = sample(num,4)
print("치킨 당첨자: {}\n치킨말고 다른거당첨자:{}".format(winners[0],winners[1:]))
