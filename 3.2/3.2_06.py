n, m = [int(input()) for _ in range(2)]
first_list = []
second_list = []
for i in range(n + m):
    if ((t := input()) in first_list):
        second_list.append(t)
    else:
        first_list.append(t)
if len(first_list) - len(second_list) == 0:
    print("Таких нет")
else:
    print("\n".join(sorted(set(first_list) - set(second_list))))