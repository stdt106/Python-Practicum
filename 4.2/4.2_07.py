def enter_results(*args):
    global list_arg
    list_arg += [x for x in args]
    return list_arg


def get_sum():
    s1 = sum(list_arg[x] for x in range(len(list_arg)) if x % 2 == 0)
    s2 = sum(list_arg[x] for x in range(len(list_arg)) if x % 2 == 1)
    return (round(s1, 2), round(s2, 2))


def get_average():
    return round(get_sum()[0] / len(list_arg) * 2, 2), round(get_sum()[1] / len(list_arg) * 2, 2)


list_arg = []