import re
p = re.compile('[a-z]+') # +는 반복
m = p.match('3 python')
print(m)