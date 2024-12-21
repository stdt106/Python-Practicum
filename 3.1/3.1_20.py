import math

m1 = [i for i in input().split()]
smbl = "+-*/~!#@"
m2 = []
for i in m1:
    if i in smbl:
        if i == "+":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(n1 + n2)
        if i == "-":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(n1 - n2)
        if i == "*":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(n1 * n2)
        if i == "/":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(n1 // n2)
        if i == "~":
            ii = m2[-1]
            m2[-1] = -ii
        if i == "!":
            n1 = m2[-1]
            m2[-1] = math.factorial(n1)
        if i == "#":
            m2.append(m2[-1])
        if i == "@":
            c1 = m2.pop(-3)
            c2 = m2.pop(-2)
            c3 = m2.pop(-1)
            m2.append(c2)
            m2.append(c3)
            m2.append(c1)
    elif i.isnumeric():
        m2.append(int(i))
print(*m2)