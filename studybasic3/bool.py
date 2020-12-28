a = [1,2,3,4]
while a:
    a.pop()   #pop는 마지막거 꺼내서 없애는 함수
    print(a)


a = [1,2,3]
b = a
a[1] = 4
print(id(a))
print(id(b))

# b는 값을 그대로 두고 a만 변경하고 싶을 때
a = [1,2,3]
b = a[:]
a[1] = 4
print(id(a))
print(id(b))