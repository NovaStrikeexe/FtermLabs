def fib(n):
    a = 0
    b = 1
    while a < n:
        a, b = b, a + b
    return a == n
n = input("input number: ")
if (fib(int(n))):
    print("It is True. It is febonacci number")
else:
    print("It is False. It is not Febonacci number")
input("Press <Enter> to close program")