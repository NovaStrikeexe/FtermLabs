y = []
x = 9
while x < 10:
    y.append(5 * x / (x * x + 81))
x += 0.01
print(max(y))