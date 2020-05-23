class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        #self.dmg= dmg
        print("{0} 유닛이 생성됐습니다.".format(self.name))
       # print("체력 {0}, 공격력 {1}".format(self.hp,self.dmg))
'''        
marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
#__init__ 은 생성자 , 인자 갯수는 맞춰서 사용
wraith1 = Unit("레이스",10,5)
print("이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.dmg))
#멤버변수를 사용할수있음
wraith2 =Unit("레ㅣ스",80,5)
wraith2.clocking = True# 외부에서 변수를 추가해서 사용가능
if wraith2.clocking ==True:
    print("{0} 는 현재 클로킹입니다.".format(wraith2.name))
'''
#메소드

class AttackUnit(Unit): # 상속
    def __init__(self,name,hp,dmg):
        Unit.__init__(self,name,hp)
        self.dmg= dmg

    def attack(self, location):
        print("{0} : {1} 방향으로 공격. [ 공격력 : {2}]".format(self.name,location,self.dmg))
    def damaged(self, damage):
        print("{0} : {1} 의 데미지를 입없습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

