'''#사전
cabinet = { 3: "a" , 100:"B"}
print(cabinet[3])
print(cabinet.get(3))
#print(cabinet[5]) => get 메소드없이 대괄호로 했다면 오류나면서 종료
#=> get 과 소괄호 사용하면 None 값 리턴
print(cabinet.get(5,"사용가능")) 
print(3 in cabinet) # true
print(5 in cabinet) # false\

c2 = {"a-1":"aaa" , "b-2" : "bbbb"}
print(c2["a-1"])

print(c2)
c2["a-1"] = "ddd"
c2["c-20"] = "ccc"
print(c2)

del c2["a-1"]
print(c2)

#key 들만 출력
print(c2.keys())
#value 만 출력
print(c2.values())
# key, value 쌍으로
print(c2.items())
# 다 지우기
c2.clear()
print(c2)
''''''
#튜플 = 고정 but fast
menu = ("a","b")
print(menu[0])
# menu.add x
name = "A"
age = 20
hobby = "AAA"
print(name,age,hobby)
(name,age,hobby) = ("A",20,"AAA")
print(name,age,hobby)
''''''
#집합 (set) 중복 x 순서 x
my_set = {1,2,3,3,3}
print(my_set)
java = {"a","b","c"}  # 아랫줄처럼 set로 정의해도 됨.
python = set(["a","b"]) 
#교집합
print(java & python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))
#add
python.add("c")
print(python)
#remove
java.remove("c")
print(java)
'''
#자료구조의 변경
menu = {"커","우","쥬"}
print(menu,type(menu))
menu = list(menu)
print(menu,type(menu))
menu = tuple(menu)
print(menu,type(menu))
menu = set(menu)
print(menu,type(menu))

