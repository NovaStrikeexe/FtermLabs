print("Start program.....")# 1.42
#Найти сумму первой и последней цифр любого целого положительного числа.
print("====================")
x = int(input("input x:"))
print("====================")
if x < 0:
    print("Your x is negative it wouldnt work")
elif x < 10:
    print("Only one simbol in list:", x)
else:
    arr = list(str(x))
    print(arr)
    print("====================")
    f = int(arr[0])
    p = int(arr[-1])
    sum = f + p
    print("Sum of first and last number =:", sum)
    print("====================")
    print("End of program")
    input("Press <Enter> to close program")