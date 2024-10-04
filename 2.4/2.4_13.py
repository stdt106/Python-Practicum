v = int(input())
d = int(input())
s = ''
c = 0
lng = len(str(v * d))
for i in range(v):
    for j in range(d):
        s += " " * (lng - len(str(i + j * v + 1))) + str(i + j * v + 1) + ' '
    s += '\n'
print(s)
