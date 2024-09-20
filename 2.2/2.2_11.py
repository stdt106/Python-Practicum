n = input()
m = [0] * 3
m[0] = n[-1]
m[1] = n[-2]
m[2] = n[-3]
m = sorted(m)
if (int(m[0]) + int(m[2])) == (int(m[1]) * 2):
    print("YES")
else:
    print("NO")
