f = open("새 파일.txt", 'r', encoding="UTF-8") 
                    #한글이 안깨지게 하기 위함.
lines = f.readlines()
for line in lines:
    print(line, end=" ")
f.close()