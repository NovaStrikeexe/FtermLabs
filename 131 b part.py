max_y = float(input("input y line: "))
if max_y > 0.278:
    """y = []
            x = 9
            while x < 10:
                y.append(5 * x / (x * x + 81))
                x += 0.01
            print(max(y))"""
    print("You used the max function! It will not work!")
else:
    x = int(input("Input epsilon"))
    a = 5 * x / (x * x + 81)
    if x < 0:
        print(x >= 0)
    elif x > a:
        print("there are no main series")
    else:
        if a > max_y:
            print("number: " + str(a))