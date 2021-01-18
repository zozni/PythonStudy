# 컴파일 옵션 MULTILINE, M
import re
p = re.compile("^python\s\w+", re.M)
#^는 맨처음이라는 뜻.
data = """python one
life is too short
python two
you need python 
python three"""

print(p.findall(data))