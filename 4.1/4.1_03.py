def number_length(num):
    if int(num) < 0:
        return len(str(num)) - 1
    return len(str(num))