from itertools import product

s = input()
no = [x for x in sorted(set(s.split())) if x.isupper()]
length = len(no)
print(*[v for v in no], "F")
for i in product([False, True], repeat=length):
    j = {key: value for key, value in zip(no, i)}
    print(*[int(v) for v in i], int(eval(s, j)))