#5.17
#Найти наибольшие общие делители (НОД) для списка кордежей, составленных из пар чисел.
#Для нахождения НОД использовать функцию.
q = int
d = int


def somfu(tuplle):
    for i in tuplle:
        if x % i == 0 and y % i == 0:
            d = i
    return d


gcd = []
tuple_list = []
sp = input("Enter the type of operation: \n2) Exit from the list filling. \n1) Continue filling in the list of tuples. :")
while sp != "2":
    if sp == "2":
        break
    elif sp == "1":
        x = int(input("Enter First item of tuple:"))
        y = int(input("Enter Second item of tuple:"))
        tuplle = (x, y)
        print("Tuple is:", tuplle)
        tuple_list.append(tuplle)
        sp = input("Enter the type of operation: \n2) Exit from the list filling. \n1) Continue filling in the list of tuples. :")
    else:
        print("Unknown operation, please choose from two necessary for you.")
        sp = input("Enter the type of operation: \n2) Exit from the list filling. \n1) Continue filling in the list of tuples. :")
print("Your List of Tuple:", tuple_list)
for tuplle in tuple_list:
    print("Your list of the greatest common divider is:", somfu(tuplle))
print("This is end.")
input("Press <Enter> to close program")

