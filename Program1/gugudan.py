# 구구단 프로그램

def GuGu(n):
    result = []
    for i in range(1,10):
        result.append(n*i)
    return result
    
print(GuGu(8))
