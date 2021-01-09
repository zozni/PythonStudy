f = open("새 파일.txt", 'a', encoding="UTF-8") 
                    #한글이 안깨지게 하기 위함.
for i in range(11,20):
    data = "%d번째 줄입네당.\n" %i
    f.write(data)
f.close()