#3.56
# В заданном списке, состоящем из целых чисел, найдите сумму и количество элементов списка, попавших в интервал [a; b].
import re# библиотека для использования регулярных вырожений
y =[]# пустой список  y
while not y:
    x = input("Input line of only integers from minus infinity to plus infinity:") #вводим строку целых чисел
    if not x:# если х = пусто
        print("The list you entered is not enough items")
    else:
        x = x.split(' ')  # разбиваем ее на отдельные элементы
        for elem in x: #проганяем элементы  списка х
            digit = re.match("^-*\d+$", elem)# проверка на пренадлежность их от -б до +б
            if digit:
                y.append(int(digit.group()))# если найден хоть один элемент присваиваем его спику у
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