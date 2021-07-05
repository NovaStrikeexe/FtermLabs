"""#3.56
# В заданном списке, состоящем из целых чисел, найдите сумму и количество элементов списка, попавших в интервал [a; b].
import re
x = (input("input line:")) #вводим список из цифр
x.split(None, maxsplit=-1)
y =[]
while not y:
    x = (input("input line:")) #вводим строку
    x = x.split(' ')
    for elem in x:
        digit = re.search("-*\d+", elem)
        if digit:
            y.append(int(digit[0]))
        else:
            print("An empty set was found performing the operation is not possible")
            x = (input("input line:"))
            x.split(None, maxsplit=-1)"""

import re
y =[]
while not y:
    x = (input("input line:")) #вводим строку
    x = x.split(' ')
    for elem in x:
        digit = re.match("^-*\d+$", elem)
        if digit:
            y.append(int(digit.string))
a = int(input("input numeral a:"))# вводим число а
b = int(input("input numeral b:"))# вводим число b
quan = 0
summ = 0
for elem in y:
    if a <= elem <= b:
        summ += elem
        quan += 1
if quan == 0:
    print("In the interval from a to b, this list does not fall into the execution of the operation is not possible")
else:
    print("Summa:", summ)
    print("Quan:", quan)
print("End of program")
input("Press <Enter> to close program")