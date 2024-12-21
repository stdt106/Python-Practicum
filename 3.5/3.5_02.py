from sys import stdin

lines = []
sr = 0
for line in stdin:
    lines.append(line.rstrip("\n"))
for i in range(len(lines)):
    before = lines[i].split()[1]
    after = lines[i].split()[2]
    sr += int(after) - int(before)
print(round(sr / len(lines)))