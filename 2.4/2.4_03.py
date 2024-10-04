n = int(input())
d = 0
m = []
for i in range(1, n + 1):
    d += 0 + i
    m.append(d)
    if d > n:
        break
s = ''
for i in range(1, n + 1):
    if i in m:
        s += str(i) + '\n'
    else:
        s += str(i) + ' '
print(s)
