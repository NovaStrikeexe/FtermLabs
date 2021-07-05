#  8.18
#  Дан символьный файл f.
#  Группы слов, разделенных пробелами (одинм или несколькими)
#  и не содержащие пробелов внутри себя,
#  будем называть словами.
#  Удалить из файла все однобуквенные слова и лишние пробелы.
#  Результат записать в файл g.
#  Медведев:
#  1) Файл создавать с нулся и туда пихать слова
#  2) Не загружать фаил в оперативу
import os.path
i = 0
y = 0
klan = 1
last = ''
eofff = 0
os.path.abspath(r"Oblivion.txt")
myfile = open(r"Oblivion.txt", "w+", encoding="cp1251")
while y != "":
    y = input("Type a word with or without space, Or leave the line blank to complete the operation: ")
    if y == "":
        break
    else:
        myfile.write(y)
myfile.seek(0)
mystring = myfile.read()
print("Text found in the inside of the file:", mystring)
#myfile.close()
while True:
    char = myfile.read(1)
    if not char:
        break
    else:
        i += 1
        print(i, char)
os.path.abspath(r"Oblivion1.txt")
myfile1 = open(r"Oblivion1.txt", "w+", encoding="cp1251")
while eofff != i:
    char1 = myfile1.read(1)
    if not char1:
        break
    else:
        fragmet = myfile.read(klan)
        if fragmet != " ":
            last += fragmet
            myfile1.write(last)
            myfile1.write(" ")
            eofff += 1
            """if len(last) >= 1:
                myfile1.write(last)
                myfile1.write(" ")
                eofff += 1"""
        if eofff == i:
            break
myfile1.close()

