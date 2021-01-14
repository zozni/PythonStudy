f = open('foo.txt', 'w')
try:                     ###시도하고
    #무언가를 수행한다.
    data = f.read()
    print(data)
except Exception as e:   ###오류났을 때 잡는거
    print(e)
finally:
    f.close()           ##무조건 마지막에 실행하는거