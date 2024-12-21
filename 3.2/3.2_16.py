f = set()
while (a := input().split()) != []:
    if len(a) > 1 and "зайка" in a:
        for i in range(len(a)):
            if a[i] == "зайка":
                if i == 0:
                    f.add(a[1])
                elif i == len(a) - 1:
                    f.add(a[-2])
                else:
                    f.add(a[i + 1])
                    f.add(a[i - 1])
print("\n".join(f))