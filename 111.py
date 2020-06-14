'''## pass 하면 완성으로 간주하고 넘어감.
class aaa:
    def __init__(self,name):
        self.name = name
        print("aaa 객체가 생성됐습니다.")

    def ppp():
        print("패스중")
        pass
        print("패스완료")
              

aaa("이름")
aaa.ppp()
'''
'''
##super() = 단일 상속일때만 사용
class Unit:
    def __init__(self):
        print("unit 생성자")


class Flyable:
    def __init__(self):
        print("flyable 생성자")

class FlyableUnit(Flyable,Unit):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()
'''
