a = input()
m = []
f = []
fr = []
mxn = 0
b = ""
while a != "ФИНИШ":
    m.append(a)
    a = input()
s = list(m)
s = ''.join(s)
s = s.replace(" ", "")
s = s.lower()
for i in s:
    n = s.count(i)
    f.append(n)
    fr.append(i)
nn = max(int(i) for i in f)
for i in f:
    if i == nn:
        print(fr[(f.index(i))])
        break