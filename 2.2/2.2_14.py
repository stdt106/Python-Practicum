n = input()
a = int(n[0])
b = int(n[1])
c = int(n[2])
m = [0] * 3
m[0] = a
m[1] = b
m[2] = c
m = sorted(m)
if m[0] == 0:
    print(m[1], m[0], " ", m[2], m[1], sep='')
else:
    print(m[0], m[1], " ", m[2], m[1], sep='')