#  8.18
#  Дан символьный файл f.
#  Группы слов, разделенных пробелами (одинм или несколькими)
#  и не содержащие пробелов внутри себя,
#  будем называть словами.
#  Удалить из файла все однобуквенные слова и лишние пробелы.
#  Результат записать в файл g.
import os.path
y = 0
last = ''
os.path.abspath(r"Oblivion.txt")
myfile = open(r"Oblivion.txt", "w+", encoding="cp1251")
myfile1 = open(r"Oblivion1.txt", "w+", encoding="cp1251")
while y != "":
    y = input("Type a word with or without space, Or leave the line blank to complete the operation: ")
    if y == "":
        break
    else:
        myfile.write(y)
myfile.seek(0)
print("Text found in the inside of the file number - 0:", myfile.read())
os.path.abspath(r"Oblivion.txt")
myfile = open(r"Oblivion.txt", "r", encoding="cp1251")
while True:
    char = myfile.read(1)
    if not char:
        break
    else:
        if char == " ":
            if len(last) != 1:
                last += " "
                myfile1.write(last)
                last = ''
            else:
                last = ''
        else:
            last += char
myfile1.seek(0)
print("Text found in the inside of the file number - 1:", myfile1.read())
myfile.close()
myfile1.close()
print("This is end.")
input("Press <Enter> to close program")