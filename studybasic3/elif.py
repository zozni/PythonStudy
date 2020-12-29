pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
# 위 식과
# message = "success" if score >= 60 else "failure" 와 같음 <조건부 표현식>
print(message)