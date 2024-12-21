d = {
    'amount': 0,
    'am_pos': 0,
    'min_num': 0,
    'max_num': 0,
    'all_sum': 0
}

c = 0
with open(input(), encoding='UTF-8') as f:
    for line in f:
        c += len(line.split())
        for i in line.split():
            d['amount'] += 1
            d['all_sum'] += int(i)
            if int(i) > 0:
                d['am_pos'] += 1
            if int(i) < d['min_num']:
                d['min_num'] = int(i)
            if int(i) >= d['max_num']:
                d['max_num'] = int(i)
print(d['amount'])
print(d['am_pos'])
print(d['min_num'])
print(d['max_num'])
print(d['all_sum'])
print(f"{(d['all_sum'] / c):.2f}")