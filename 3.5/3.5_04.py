from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
search = lines.pop(-1)
for line in lines:
    if search.lower() in line.lower():
        print(line)