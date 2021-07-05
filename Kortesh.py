#5.17
#Найти наибольший общий делитель (НОД) для списка кордежей, составленных из пар чисел.
#Для нахождения НОД использовать функцию.
q = int
d = int
def somfu(x,y):
    for tuplle in tuple_list:
        for i in tuplle:
            if x % i == 0 and y % i == 0:
                d = i
    return d


gcd = []
tuple_list = []
while tuple_list != "stop":
    x = int(input("Enter First item of tuple:"))
    y = int(input("Enter Second item of tuple:"))
    tuplle = (x, y)
    print("Tuple is:", tuplle)
    tuple_list.append(tuplle)
    if tuple_list == "stop":
        break
    else:
        print("Your List of Tuple:", tuple_list)
        print("Now lets start work with next.")
        print("Enter a tuple or write stop to stop entering.")
for tuplle in (tuple_list):
    print("Your list of the greatest common divider is:", somfu(d))
print("This is end.")
input("Press <Enter> to close program")