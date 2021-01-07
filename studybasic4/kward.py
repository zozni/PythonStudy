def print_kwargs(**kwargs): #keyward arguments
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + k)
print(print_kwargs(name="int 조수", b="2"))