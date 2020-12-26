import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = random.randint(1,360) #1~360에서 아무 수나 골라 a에 저장한다
    t.setheading(a)
    b = random.randint(1,20)
    t.fd(b)
    
