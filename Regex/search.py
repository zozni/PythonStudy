import re
p = re.compile('[a-z]+') # +는 반복
m = p.search('3 python')
print(m)