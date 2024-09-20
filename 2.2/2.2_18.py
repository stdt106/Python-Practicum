a = int(input())
b = int(input())
c = int(input())
m = [0] * 3
m[0] = a
m[1] = b
m[2] = c
m = sorted(m)
if (m[2] ** 2) < ((m[0] ** 2) + (m[1] ** 2)):
    print("крайне мала")
elif (m[2] ** 2) == ((m[0] ** 2) + (m[1] ** 2)):
    print("100%")
else:
    print("велика")