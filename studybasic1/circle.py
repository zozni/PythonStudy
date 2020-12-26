import turtle as t

n=50
t.bgcolor("black")  #배경색을 검은색으로 지정
t.color("green")
t.speed(0)  #거북이 속도를 가장 빠르게 지정
for x in range(n):
    t.circle(80)
    t.lt(360/n)
