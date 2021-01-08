def add(a,b):
    return a+b

add = lambda a, b: a+b #리스트 안에서도 정의가 가능
                       #위 두개는 같은 코드임.
print(add(1,2))

myList = [lambda a, b: a+b, lambda a,b: a*b]
#myList[0] #이게 a+b 함수를 불러온거임. 개쩐다. 함수 이름도 없음
print(myList[0](1,2))