def add_number(number):
    global m
    m.append(number)


def get_sum():
    s = ""
    sm = 0
    for i in m:
        s += str(i) + " + "
        sm += i
    return s[:-3] + " = " + str(sm)


m = []