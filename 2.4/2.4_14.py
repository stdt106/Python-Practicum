v = int(input())
d = int(input())
s = ''
lng = len(str(v * d))
for i in range(1, v + 1):
    for j in range(1, d + 1):
        if i % 2 == 0:
            s += " " * (lng - len(str(d * i - j + 1))) + str(d * i - j + 1) + ' '
        else:
            s += " " * (lng - len(str(d * (i - 1) + j))) + str(d * (i - 1) + j) + ' '
    s += '\n'
print(s)
