v = int(input())
d = int(input())
s = ''
lng = len(str(v * d))
for i in range(1, v * d + 1):
    if i % d == 0:
        s += " " * (lng - len(str(i))) + str(i) + '\n'
    else:
        s += " " * (lng - len(str(i))) + str(i) + ' '
print(s)
