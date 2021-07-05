#4.22
# В классе учится n учеников.
# Известны их имена.
# Известно так же кто был в гостях у Кати, кто был у Васи и т.д.
# Определить, есть ли в классе хотя бы один человек, который не был в гостях ни у кого из своих одноклассников.
# Если есть такие ученики, то вывести их имена, если нет, то сообщить об этом.
# PS Катя и Вася Меняются на  английские аналоги ()()ps from NOVA_STRIKE.exe() ()
z = 0
p = 1
v = []
Class = []
guest = ()
x = ()
Quantity = int(input("Enter the number of students per group:"))
while len(Class) != Quantity:
    x = input("Enter student in group:")
    Class.append(x)
for z in range(0, Quantity):
    z += 1
    v.append(z)
My_Class = dict(zip(v, Class))
print("My group is: ", My_Class)
while p != Quantity + 1:
    print("Its: ", My_Class[p])
    My_Class[p] = []
    while guest != "stop":
        guest = input("Enter the name of the student who was visiting him \n(or write a stop to complete this operation):")
        if guest == "stop":
            guest = " "
            break
        else:
            My_Class[p].append(guest)
    p += 1
print("This is end.")
input("Press <Enter> to close program")








