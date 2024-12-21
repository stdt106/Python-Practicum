d = {}
for i in range(n := int(input())):
    n, t = (s := input()).split(": ")
    t = set(t.split(", "))
    for j in t:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
d = sorted(d.items(), key=lambda x: x[0])
for k, v in d:
    if v == 1:
        print(k)