# 전방탐색: 긍정형 (?=)
import re
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())