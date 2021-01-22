# 전방탐색: 부정형 (?!)
import re
p = re.compile(".*[.](?!bat$|exe$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)