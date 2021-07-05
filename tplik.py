#5.17
#Найти наибольшие общие делители (НОД) для списка кордежей, составленных из пар чисел.
#Для нахождения НОД использовать функцию.


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


z = 0
tuple_list = []
while True:
    x = input("Enter First item of tuple:")
    y = input("Enter Second item of tuple:")
    if not x.isdigit() or not y.isdigit():
        break
    else:
        z += 1
        tuplle = (int(x), int(y))
        print("Tuple is number:", z, tuplle)
        print("You can continue to add tuples to the list\nOr leave empty the first and the second element of the tuple\nTo stop the input operation.")
        tuple_list.append(tuplle)
print("Your List of Tuple:", tuple_list)
for elem in tuple_list:
    a = elem[0]
    b = elem[1]
    gcd(a, b)
    print("Your list of the greatest common divider is:", gcd(a, b))
print("This is end.")
input("Press <Enter> to close program")
