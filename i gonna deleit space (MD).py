#2.32.
#  Во введенной строке удалить пробелы между первым и вторым вопросительным знаком.
print("Hello user:")
a = input ("Input Line: ")#Вводим линию из рандомных символов
b = input("\n\nInput Symbol:")#Вводим символ
symbolmark = a.find(b)
symbolmark1 = a.find(b, symbolmark + 1);
a1 = a[:symbolmark + 1]
a2 = a[symbolmark + 1:symbolmark1]
a3 = a[symbolmark1:]
a2 = a2.replace(" ","")
a4 = a1 + a2 + a3
print("\nLine before change : -------------> ", a, "\nLine after change: ------------> ", a4, end = " ")
print("End of program")
input("\nPress <Enter> to close program")