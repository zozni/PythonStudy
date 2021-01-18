# 컴파일 옵션 DOTALL, S
import re
p = re.compile('a.b', re.DOTALL) #dot은 줄바꿈을 제외한 모든 문자와 매치됨.
m = p.match('a\nb') #줄바꿈 문자가 포함됨.
print(m)