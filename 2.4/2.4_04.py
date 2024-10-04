N = int(input())
s = 0
for i in range(N):
    a = int(input())
    s += sum(map(int, str(a)))
print(s)