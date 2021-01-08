def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself(old=23, name="zozni", man=False)