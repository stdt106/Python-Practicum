mm = []
for i in range(int(input())):
    m = []
    while (x := input()) != "next":
        m.append(int(x))
    mm.append(sum(m) / len(m))
print('%.2f' % max(mm))
