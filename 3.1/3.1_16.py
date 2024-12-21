dl, n = int(input()), int(input())
for i in range(n):
    a = input()
    if len(a) >= dl - 3:
        print(a[:dl - 3] + "...")
        break
    else:
        dl -= len(a)
        print(a)