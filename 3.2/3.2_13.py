d = {}
dn = {}
m = set()
t = 0
for i in range(n := int(input())):
    if (a := input()) in d:
        d[a] += 1
    else:
        d[a] = 1
for i in range(n1 := int(input())):
    for j in range(n2 := int(input())):
        if (a := input()) in dn:
            dn[a] += 1
        else:
            dn[a] = 1
s1 = set(d.keys())
s2 = set(dn.keys())
for i in s1:
    if i not in s2:
        m.add(i)
mm = [i for i in m]
if mm:
    print("\n".join(sorted(m)))
else:
    print("Готовить нечего")
