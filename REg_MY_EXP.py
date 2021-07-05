#6.17 Проверить существуют ли в тексте цифры, за которыми стоит «+».
# Пример правильного выражения: (3 + 5) – 9×4.
# Пример неправильного выражения: 2 * 9 – 6 × 5.
import re
print("This program check your expression for text numbers behind which is a +.")
strik = input("Please, Enter your expression:")
p = re.compile(r"[0-9]\s*\+")
if p.search(strik):
    print("Your expression is correct,there are text numbers behind which is a +.")
else:
    print("Your expression is incorrect, there are no text behind which there is a +.")
print("This is end.")
input("Press <Enter> to close program")