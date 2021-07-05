#2.42
#Дана строка. Подсчитать общее количество содержащихся в ней СТРОЧНЫХ латинских и русских букв.
print("Start program.....")
arr = (input("Input some line of Letters with Cyrillic and Latin:"))
print("The entire length of the string:",len(arr))
lat = 0;
cir = 0;
for letter in arr:
#for i in range(arr(a)):
    if ord(letter) in range(97, 123):
        lat += 1
    elif ord(letter) in range(1072, 1104):
        cir += 1
print("Number of Latin:", lat)
print("Number of Cirilic:", cir)
print("====================")
print("End of program")
input("Press <Enter> to close program")
