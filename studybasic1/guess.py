import random

n = random.randint(1,30)

while True:    #이렇게 하면 무한반복
    x = input("맞혀 보세요! 1~30")
    g = int(x)
    if g == n:
        print("정답!")
        break   #g==n일때 break로 while문 탈출 
    if g > n:
        print ("너무 커요")
    if g < n:
        print ("너무 작아요")
