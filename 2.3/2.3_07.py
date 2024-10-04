a = int(input())
b = int(input())
for i in range(1, 10000000):
    if i % a == 0 and i % b == 0:
        ii = i
        break
print(ii)