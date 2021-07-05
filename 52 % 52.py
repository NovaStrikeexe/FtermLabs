#3.72
#Даны два пятизначных числа,
#необходимо найти количество совпадений по две одинаковые цифры в равносильных разрядах чисел,
#а так же количество совпадений по две одинаковые цифры в различных разрядах этих чисел.
#Цифра, которая уже участвовала в одной паре совпадения, не учитывается повторно.
z = 0
e = 0
my_list = []
my_list1 = []
while len(my_list) != 5:
    my_list = input("Enter a positive five-digit number 1:")
    if len(my_list) != 5:
        print("The entered number is not a five-digit further execution of operations is not possible")
        my_list = input("Enter a positive five-digit number 1:")
while len(my_list1) != 5:
    my_list1 = input("Enter a positive five-digit number 2:")
    if len(my_list1) != 5:
        print("The entered number is not a five-digit further execution of operations is not possible")
        my_list1 = input("Enter a positive five-digit number 2:")
my_list = list(my_list)
my_list1 = list(my_list1)
print("First number:", my_list)
print("Second number:", my_list1)
check_list = [0,0,0,0,0]
for i in range(5):
    if my_list[i] == my_list1[i]:
        e += 1
        check_list[i] = 1
for i in range(5):
    for j in range (5):
        if check_list[i]==0:
            if my_list[i] == my_list1[j] and check_list[j] == 0:
                z += 1
                check_list[j] = 1
                break
print("Number of bit-matched matches is:",e)
print("Total matched numbers is:",z)
print("End of program")
input("Press <Enter> to close program")