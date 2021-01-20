# 메타문자 |
import re
p = re.compile('Crow|Servo') #앞에거 또는 뒤에거가 일치할때
m = p.match('CrowHello')
print(m)