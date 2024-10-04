v = int(input())
d = int(input())
s = ''
c = 0
lng = len(str(v * d))
for i in range(1, v + 1):
    for j in range(d):
        if j % 2 != 0:
            s += " " * (lng - len(str(v + j * v - i + 1))) + str(v + j * v - i + 1) + ' '
        else:
            s += " " * (lng - len(str(i + j * v))) + str(i + j * v) + ' '
    s += '\n'
print(s)
