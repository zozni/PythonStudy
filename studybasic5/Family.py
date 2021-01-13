class Family:
    lastname = "김" #클래스 변수

Family.lastname = "박" #설계도 자체가 박으로 바뀜.
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)