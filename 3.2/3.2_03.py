s = set()
for i in range(n := int(input())):
    st = input().split()
    for j in st:
        s.add(j)
for i in s:
    print(i)