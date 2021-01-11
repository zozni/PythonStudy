result = 0
def add(num):
    global result  #전역변수
    result += num
    return result

print(add(3))
print(add(4))