n = str(input())
m = str(input())
if len(n) == 2:
    n = "0" + n
if len(m) == 2:
    m = "0" + m
if len(n) == 1:
    n = "00" + n
if len(m) == 1:
    m = "00" + m
s = str(int(n[0]) + int(m[0]))[-1] + str(int(n[1]) + int(m[1]))[-1] + str(int(n[2]) + int(m[2]))[-1]
print(s)