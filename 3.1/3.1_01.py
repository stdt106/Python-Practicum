n = int(input())
c = 0
for i in range(n):
    x = input()
    if x[0] == "а" or x[0] == "б" or x[0] == "в":
        c += 1
if c == n:
    print("YES")
else:
    print("NO")