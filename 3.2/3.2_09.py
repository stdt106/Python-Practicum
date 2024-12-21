d = {}
s = ''
while (a := input()) != "":
    s += a + " "
s = s.split()
for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for i in d:
    print(i, d[i])
