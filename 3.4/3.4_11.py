from itertools import product

s = ""
d, v = int(input()), int(input())
mxs = len(str(d * v))
nn1 = [f"{x[1] + v * (x[0] - 1)}" for x in list(product([x for x in range(1, d + 1)], list(range(1, v + 1))))]
nn = " ".join(nn1).split()
for i in nn:
    if len(s.split()) == v - 1:
        s += " " * (mxs - len(i)) + i
        print(s)
        s += "\n"
        s = ""
    else:
        s += " " * (mxs - len(i)) + i + " "