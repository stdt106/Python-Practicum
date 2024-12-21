def gcd(*numbers):
    mn = min(numbers)
    while len(numbers) != len([x for x in numbers if x % mn == 0]):
        mn -= 1
    return mn