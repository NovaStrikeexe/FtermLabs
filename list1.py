#3.56
# В заданном списке, состоящем из целых чисел, найдите сумму и количество элементов списка, попавших в интервал [a; b].
y =[]
while not y:
    x = input("Input line of only integers from minus infinity to plus infinity:") #вводим строку целых чисел
    if not x:# если х = пусто
        print("The list you entered is not enough items")
        x = input("Input line of only integers from minus infinity to plus infinity:")
    else:
        y = True
a = float(input("input numeral a:"))# вводим число а
b = float(input("input numeral b:"))# вводим число b
quan = 0
summ = 0
x = x.split(' ')  # разбиваем ее на отдельные элементы
for i in x:
    if a <= i <= b:
        summ += i
        quan += 1
if quan == 0:
    print("In the interval from a to b, this list does not fall into the execution of ")
else:
    print("Summa:", summ)
    print("Quan:", quan)
print("End of program")
input("Press <Enter> to close program")