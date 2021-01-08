a = 1
def vartest(a):  #이 함수안에 변수는 이 안에서만 쓰인다.
    a = a+1
    return a
a = vartest(a) #해결 방법 
print(a)

b = 1
def vartest_1():
    global b
    b = b+1
vartest_1()
print(b)