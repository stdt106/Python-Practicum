d = dict()
m = []
while (n := input()) != '':
    m += list([i.upper() for i in n.split()])
for i in m:
    if len(i) % 2 == 0:
        if i[int(len(i) / 2) // 1 - 1] in d:
            d[i[int(len(i) / 2) // 1 - 1]].add(i)
        else:
            d[i[int(len(i) / 2) // 1 - 1]] = {i}
    elif len(i) % 2 != 0:
        if i[int(len(i) / 2) // 1] in d:
            d[i[int(len(i) / 2) // 1]].add(i)
        else:
            d[i[int(len(i) / 2) // 1]] = {i}
for i in d:
    p = '"' + '. '.join(sorted(d[i])) + '"'
    print(f'{i.lower()} {p}')



'''
А лисички
Взяли спички
К морю синему пошли
Море синее зажгли
Море пламенем горит
Выбежал из моря кит
Эй пожарные бегите
Помогите помогите

'''
