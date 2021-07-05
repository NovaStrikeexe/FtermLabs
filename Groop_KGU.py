# 7.22
# Опишите, используя словарь, анкету школьника (фамилия, возраст).
# Определите возрастные группы в классе и напечатайте их списки.
dps = {}
while True:
    print("Enter the student's name and age \nOr type a stop in both fields.")
    pupil = input("Enter class student: ")
    year = input("Enter this student's age: ")
    if pupil == "stop" and year == "stop":
        print("Logging complete.")
        break
    else:
        if year not in dps:
            dps.setdefault(year, []).append(pupil)
        else:
            dps.setdefault(year, []).append(pupil)
        print("Student Added to Journal.")
print("Students in the class: ", dps)
print("All students yeargroup in journal:")
for key in sorted(dps.keys()):
    print("({0}:{1})".format(key, dps[key]), end=" ")
"""y = input("Enter the age of students whose names you want to see: ")
g = dps.setdefault(y)
print("It,s your year group:", g)
print("This is end.")
input("Press <Enter> to close program")"""
print("This is end.")
input("Press <Enter> to close program")

