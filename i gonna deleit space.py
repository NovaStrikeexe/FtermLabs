#2.32.
#  Во введенной строке удалить пробелы между первым и вторым вопросительным знаком.
import re
print("Start program.....")
a = input("Input line of simbols with some symbols of ?:")
print(re.findall("\?\w* +\w*\?", a))
print(a + "    ------->    " + re.sub("\?\w* +\?", "??", a))
print("End of program")
input("\nPress <Enter> to close program")