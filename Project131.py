#1.31
#A
import matplotlib.pyplot as plt
print("Start program.....")
from pylab import *
def summa(n):
    sum = 0
    for i in range(1, n+1):
        a = 5*i/(i*i+81)
        sum += a
    print("Sum: " + str(sum))
summa(5)
#B
E = float(input("Imput Epsilon:"))
if E <= 0:
    print("All the terms of the series of numbers>" E)
else:
    k = 1
    a = 5 * k / (k * k + 81)
    if E > a:
    print("There is no series of numbers >", E)
    else:
        while E <= a:
            print(a)
            k += 1
            a = 5 * k / (k * k + 81)
print("This end.")
input("Press <Enter> to close program")



