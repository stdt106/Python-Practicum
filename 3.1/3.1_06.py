n = int(input())
c = 0
for i in range(n):
    x = input()
    if "зайка" in x:
        if x.count("зайка") > 1:
            c += x.count("зайка")
        else:
            c += 1
print(c)