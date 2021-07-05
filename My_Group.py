# 4.22
# В классе учится n учеников.
# Известны их имена.
# Известно так же кто был в гостях у Кати, кто был у Васи и т.д.
# Определить, есть ли в классе хотя бы один человек, который не был в гостях ни у кого из своих одноклассников.
# Если есть такие ученики, то вывести их имена, если нет, то сообщить об этом.
# PS Катя и Вася Меняются на  английские аналоги ()()ps from NOVA_STRIKE.exe()
z = 0
v = []
group = []
guest = ()
x = ()
My_vis_set = set()
quantity = int(input("Enter the number of students per group:"))
while len(group) != quantity:
    x = input("Enter student in group:")
    group.append(x)
My_group = set(group)
print("My group is: ", My_group)
for elem in My_group:
    print("Its: ", elem)
    while guest != "stop":
        guest = input("Enter the name of the student who was visiting him \n(or write a stop to complete this operation):")
        if guest == "stop":
            guest =" "
            break
        else:
            My_vis_set.add(guest)
print("People who have not been a guest:",My_group.difference(set(My_vis_set)))
print("People who were visiting:",My_group.intersection(set(My_vis_set)))
print("This is end.")
input("Press <Enter> to close program")
""" if guest == "stop":
            guest = " "
            break
    elif guest not in My_Group:
                print("This person is not in a group,\nPlease enter people who study only in this group.")
                guest = input("Enter the name of the student who was visiting him \n(or write a stop to complete this operation):")
    else:
            My_Group[p].append(guest)"""