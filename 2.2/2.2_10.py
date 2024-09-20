a = int(input())
ed = a % 10 + a % 100 // 10
ds = a % 100 // 10 + a // 100
print(max(ed, ds), min(ed, ds), sep='')