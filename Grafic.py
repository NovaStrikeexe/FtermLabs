import matplotlib.pyplot as plt
from pylab import *
def func(n):
    k = 1
    y = 0
    x = 0
    x2 = 21
fig, ax = plt.subplots()
x = linspace(1, 100, 100)
y = 5 * x / (x * x + 81)
z = y + x * 0
ax.plot(x, y, 'r')
ax.plot(x, z)
xlabel('x')
ylabel('y')
show()
input("Press <Enter> to close program")