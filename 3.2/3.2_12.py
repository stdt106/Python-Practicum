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
c = l = 0
d = {}
for sur, count in dict.items():
    l += 1
    if count > 1:
        d[sur] = count
        c += 1
    elif count == 1 and c == 0 and l == len(dict):
        print("Однофамильцев нет")
        break
sk = sorted(d.items(), key=lambda x: x[0])
for sur, count in sk:
    print(f"{sur} - {count}")