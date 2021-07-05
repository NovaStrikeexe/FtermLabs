#3.56
# В заданном списке, состоящем из целых чисел, найдите сумму и количество элементов списка, попавших в интервал [a; b].
y = []
x = ()
while x != "stop fill":
    x = input("Input integer or write (stop fill) to complite inputing:")
    if x =="stop fill":
        break
    else:
        y.append(x)
print("Ready list is:", y)
a = float(input("input numeral a:"))  # вводим число а
b = float(input("input numeral b:"))  # вводим число b
quan = 0
summ = 0
for (i) in y:
    if a <= float(i) <= b:
        summ += float(i)
        quan += 1
if quan == 0:
    print("In the interval from a to b, this list does not fall into the execution ")
else:
    print("Summa:", summ)
    print("Quan:", quan)
print("End of program")
input("Press <Enter> to close program")

