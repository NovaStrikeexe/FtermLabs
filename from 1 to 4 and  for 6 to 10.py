#3,68
#Дан список из 10 элементов. Первые 4 упорядочить по возрастанию, последние 4 по убыванию.
y = 0
while y != 1 or y != 2:
    y = int(input("Choice type of operation: \n1) Operation with numbers. \n2) Operation with letters."))
    if not y:# если y = пусто
        print("You dont chouse command")
        y = int(input("Choice type of operation: \n1) Operation with numbers. \n2) Operation with letters."))
    else:
        if y == 1:
            print("Your choice is 1:\nOperation with numbers ")
            x = input("Input line of ten elemets: ")
            x = x.split(' ')  # разбиваем ее на отдельные элементы
            if len(x) < 4:
                print("The list you entered is not enough items")
                x = input("Enter a list of no more than 10 characters ")
            elif len(x) <= 10:
                a = x[: 4]
                a = sorted(a, key=int)
                print("First four elements:", a)
                b = x[-4:]#same as that len(x)-4
                b = sorted(b, key=int, reverse=True)
                print("Last four elements:", b)
                if len(x) == 4:
                    print("List line = 4 i dont gonna print it")
                else:
                    x[0:] = a + b
                print(x)
            else:
                len(x) > 10
                print("The list you entered is too many items")
                x = input("Enter a list of no more than 10 characters ")
            break
        elif y == 2:
            print("Your choice is 2:\nOperation with letters")
            x = input("Input line of ten elemets: ")
            x = x.split(' ')  # разбиваем ее на отдельные элементы
            if len(x) < 4:
                print("The list you entered is not enough items")
                x = input("Enter a list of no more than 10 characters ")
            elif len[x] < 10:
                a = x[: 4]
                a = sorted(a,)
                print("First four elements:", a)
                b = x[-4:]#len(x) - 4
                b = sorted(b, reverse=True)
                print("Last four elements:", b)
                x[0:] = a + b
                print(x)
            else:
                len(x) > 10
                print("The list you entered is too many items")
                x = input("Enter a list of no more than 10 characters ")
            break
print("End of program")
input("Press <Enter> to close program")