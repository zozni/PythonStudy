import re
p = re.compile('[a-z]+') # +는 반복
m = p.findall('life is too short')
print(m)