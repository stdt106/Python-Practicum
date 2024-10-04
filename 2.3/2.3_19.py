print(500)
p = 501
ng = 0
vg = 1001
g = input()
for i in range(10):
    if g == "Меньше":
        vg = p
        p = p - (p - ng) // 2
    if g == "Больше":
        ng = p
        p = p + (vg - p) // 2
    print(p)
    g = input()
    if g == "Угадал!":
        break