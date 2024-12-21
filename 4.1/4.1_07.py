def can_eat(t1, t2):
    tt1 = abs(t1[0] - t2[0]) == 2 and abs(t1[1] - t2[1]) == 1
    tt2 = abs(t1[0] - t2[0]) == 1 and abs(t1[1] - t2[1]) == 2
    if tt1 or tt2:
        return True
    else:
        return False