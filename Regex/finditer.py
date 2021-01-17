import re
p = re.compile('[a-z]+') # +는 반복
m = p.finditer('life is too short')
for r in m:
    print(r)
