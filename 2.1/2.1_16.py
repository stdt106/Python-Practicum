a = int(input())
b = int(input())
c = int(input())
r = str((b - a) / c)
if r[-2] == ".":
    r = r + "0"
print(r)