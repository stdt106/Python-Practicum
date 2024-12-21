dict = {}
s = ""
c = 0
for i in range(n := int(input())):
    s += (a := input()) + " "
for i in (s.split()):
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for sur, count in dict.items():
    if count > 1:
        c += count
print(c)