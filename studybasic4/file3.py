f = open("새 파일.txt", 'r', encoding="UTF-8") 
                    #한글이 안깨지게 하기 위함.
while True:
    line = f.readline()
    if not line: break #line이 없으면 break.
    print(line)
f.close()