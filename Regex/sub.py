# 문자열 바꾸기 sub
import re
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')