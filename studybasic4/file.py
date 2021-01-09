f = open("새 파일.txt", 'w', encoding="UTF-8") 
                    #한글이 안깨지게 하기 위함.
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()