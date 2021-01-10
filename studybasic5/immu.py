######Immutable#####
a = 1         #지역변수
def vartest(a):
    a =a+1
vartest(a)
print(a)
#####################

#####Mutable#########
b = [1,2,3]  #전역변수
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)
#####################