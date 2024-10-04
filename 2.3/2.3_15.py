n = int(input())
c = 0
for i in range(n):
    s = input()
    if "зайка" in s:
        c += s.count("зайка")
print(c)