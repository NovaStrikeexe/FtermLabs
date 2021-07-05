#3.49
#Дано натуральное число n>=2, список списков, состоящий из n элементов по n чисел в элементе.
# Список заполняется случайным образом числами из промежутка от 0 до 199.
# Найти количество всех двухзначных чисел, у которых сумма цифр кратна 2.
import random
i = 0
z = 0
j = 0
n = 0
n = int(input("Enter the number of columns from 2 and more:"))
while n < 2:
    print("The array must consist of at least two columns !")
    n = int(input("Enter the number of columns from 2 and more:"))
m = [[random.randint(0,200) for _ in range(0,n)] for _ in range(0, n)]
print("Massive m:","\n",m)
for lst in m:
    for elem in lst:
        if 10 < elem < 100:
            f = elem // 10
            i = elem % 10
            #f = int(elem[0])
            #p = int(elem[-1])
            summa = f + i
            if summa % 2 == 0:
                z += 1
        #print(elem)
print("The number of all two-digit numbers whose sum of digits is a multiple of 2 =", z)
print("End of program")
input("Press <Enter> to close program")