s = [x for x in input().split()]
print("a b c f")
x = [
    0, 0, 0,
    0, 0, 1,
    0, 1, 0,
    0, 1, 1,
    1, 0, 0,
    1, 0, 1,
    1, 1, 0,
    1, 1, 1,
]
for i in range(0, len(x), 3):
    ss = " ".join([j for j in s]).replace("a", "x[i]", 1).replace("b", "x[i + 1]", 1).replace("c", "x[i + 2]", 1)
    print(x[i], x[i + 1], x[i + 2], int(eval(ss)))
