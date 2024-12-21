from itertools import product


def grasshopper(start, finish, length):
    tt = []
    for i in product([1, -1, 2, -2], repeat=length):
        if sum(i) == finish - start:
            t = [start]
            for j in i:
                t.append(t[-1] + j)
            tt.append(t)
    rr = []
    for i in tt:
        if i.count(finish) == 1:
            rr.append(i)
    return rr
