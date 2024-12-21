m = []
with open(input(), encoding="UTF-8") as file_in:
    for line in file_in:
        m.append(line.replace("\t", "").split())
with open(input(), "w", encoding="UTF-8") as ww:
    for i in m:
        if i != []:
            ww.write(' '.join(i) + '\n')