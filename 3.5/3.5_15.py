import json


with open("scoring.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
c = 0
right_ans = []
for d in range(len(records)):
    for t in records[d]["tests"]:
        c += 1
        right_ans.append([t["pattern"], records[d]["points"] // len(records[d]["tests"])])
inp_ans = [input() for _ in range(c)]
points = 0
for i in range(c):
    if inp_ans[i] == right_ans[i][0]:
        points += right_ans[i][1]
print(points)