def find_pair(*numbers, div=6):
    s = (0, 0)
    ind = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % div == 0:
                if (numbers[i] + numbers[j]) >= (s[0] + s[1]):
                    if (numbers[i] + numbers[j]) == (s[0] + s[1]):
                        if j > ind:
                            s = (numbers[i], numbers[j])
                            ind = j
                    else:
                        s = (numbers[i], numbers[j])
                        ind = j
    return s