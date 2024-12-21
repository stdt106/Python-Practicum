m1 = [i for i in input().split()]
num = "0123456789"
smbl = "+-*"
m2 = []
for i in m1:
    if i in smbl:
        if i == "+":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(int(n1) + int(n2))
        elif i == "-":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(int(n1) - int(n2))
        elif i == "*":
            n1 = m2.pop(-2)
            n2 = m2.pop(-1)
            m2.append(int(n1) * int(n2))
    else:
        m2.append(i)
print(*m2)
