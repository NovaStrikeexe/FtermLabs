import math
for abc in range(100, 1000):
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    p = math.factorial(a)
    h = math.factorial(b)
    x = math.factorial(c)
    if abc == p + h + x:
        print(str(abc))
