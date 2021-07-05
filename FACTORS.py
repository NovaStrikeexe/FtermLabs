#Найти все делители натурального числа
print("Start program.....")
x = int(input("input x:"))
def print_factors(x):
    print(" The factors of ", x, "are:")
    for z in range(1, x + 1):
        if x % z == 0:
            print(z)
print_factors(x)
print("End of program")
input("Press <Enter> to close program")