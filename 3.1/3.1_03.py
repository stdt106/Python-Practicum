L = int(input())
N = int(input())
for i in range(N):
    x = input()
    if len(x) > L:
        print(x[:(L - 3)] + "...")
    else:
        print(x)
