s1, s2 = input().split(), input().split()
s = list(zip(s1, s2))
for i in s:
    print(' - '.join(str(k).replace(',', '') for k in i))