import turtle
import sys

TITLE="파이썬 거북이로 별 그리기"

START_X = -100
START_Y= 100

if TITLE == '':
    print("TITLE이 없습니다.")
    sys.exit(0)

if START_X <-100 or START_X>300:
    print("START_X 는 -300과 300사이 입니다.")
    sys.exit(0)

if START_Y <-300 or START_Y > 300:
    print("START_Y는 -300 과 300 사이입니다.")
    sys.exit(0)

turtle.title(TITLE)
turtle.penup()
turtle.setx(START_X)
turtle.sety(START_Y)
turtle.pendown()

turtle.color('blue', 'yellow')
turtle.begin_fill()
while True:
    turtle.fd(200)

    turtle.lt(360*2/5)

    if abs(turtle.distance(START_X, START_Y)) <1:
        break

turtle.end_fill()
turtle.done()
