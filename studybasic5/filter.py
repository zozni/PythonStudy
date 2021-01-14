def positive(x):
    return x > 0

a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)
