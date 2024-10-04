n = int(input())
c = cmx = cc = 0
for i in range(n):
    c = 0
    a = input()
    if a == "зайка":
        c += 1
        cmx = max(cmx, c)
    while a != "ВСЁ":
        a = input()
        if a == "зайка":
            c += 1
            cmx = max(cmx, c)
    if c >= 1:
        cc += 1
print(cc)