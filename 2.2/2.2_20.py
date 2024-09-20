a = input()
b = input()
c = input()
m = [0] * 3
m[0] = a
m[1] = b
m[2] = c
m = sorted(m)
for i in range(3):
    if "зайка" in m[i]:
        print(m[i], len(m[i]))
        break