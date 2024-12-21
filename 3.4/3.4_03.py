from itertools import count

t_start, t_stop, t_step = input().split()
for value in count(float(t_start), float(t_step)):
    if value <= float(t_stop):
        print(f"{value:.2f}")
    else:
        break