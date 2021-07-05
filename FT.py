def summa (a =2, b=3, c=4):
    return a + b + c
t =(1,2)
d = {"c" : 3}
print(summa(**d, *t))