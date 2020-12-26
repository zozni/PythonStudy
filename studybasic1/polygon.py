import turtle as t

n=5
t.color("orange")
t.begin_fill()  #색칠할 영역을 시작합니다.
for x in range(n):
    t.fd(50)
    t.lt(360/n)
t.end_fill()  #색칠할 영역을 마무리합니다.
