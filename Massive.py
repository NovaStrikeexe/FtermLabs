import random
n = 0
n = int(input("Enter the number of columns from 2 and more:"))
if n < 2:
    print("The array must consist of at least two columns !")
    n = int(input("Enter the number of columns from 2 and more:"))
else:
    m = [][]
    for i in range(0, n):
        for j in range(0, n):
            m[i][j] = random.randint(0, 200)
            print("Massive m:\n", m)
"""n = 0
n = int(input("Enter the number of columns from 2 and more:"))
while n < 2:
    print("The array must consist of at least two columns !")
    n = int(input("Enter the number of columns from 2 and more:"))
#int N.random(0, 200)
m = [[n for _ in range(0, n)] for _ in range(0, n)]
print(m)"""