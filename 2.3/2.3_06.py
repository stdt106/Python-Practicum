a = int(input())
b = int(input())
for i in range(1, max(a, b + 1)):
    if a % i == 0 and b % i == 0:
        ii = i
print(ii)