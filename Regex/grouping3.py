# 그룹핑()
import re
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())