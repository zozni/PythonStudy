try:
    f = open("없는 파일", 'r')
except FileNotFoundError:
    pass