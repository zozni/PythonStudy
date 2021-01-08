#for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number = number + 1
    if mark < 60 : 
        continue #if에 걸리면 그냥 넘어가 
    print("%d번 학생 축하합니다. 합격입니다." %number) 
     #if에 안결렸으니까 출력됨.