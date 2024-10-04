a = int(input())
s = ''
c = 1
for i in range(1, a + 1):
    for h in range(1, a + 1):
        if c % a == 0:
            s += str(i * h) + " " + "\n"
            c += 1
        else:
            s += str(i * h) + " "
            c += 1
print(s)
