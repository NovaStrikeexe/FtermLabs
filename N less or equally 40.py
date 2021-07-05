def print_factors(i):
    print(" The factors of ", i, "are:")
    for z in range(1, i + 1):
        if i % z == 0:
            print(z)
N = int(input("Input N:"))
for i in range(1, N+1):
    print_factors(i)






