x = "6493905658"
#x = "abcdltuidq"
print(x)
head = sorted(x[:4])
tail = sorted(x[-4:], reverse=True)
if len(x)-4 >= 4:
    first_stop = 4
else:
    first_stop = len(x)-4
result = head[:first_stop]
if len(x)>8:
    center = len(x)-8
    for i in range(center):
        result.append(x[4+i])
result += tail
print(result)