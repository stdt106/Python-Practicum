def is_palindrome(s):
    if isinstance(s, str):
        if s == s[::-1]:
            return True
        else:
            return False
    if isinstance(s, int):
        if str(s) == str(s)[::-1]:
            return True
        return False
    if isinstance(s, tuple):
        if tuple(reversed(s)) == s:
            return True
        else:
            return False
    if isinstance(s, list):
        if list(reversed(s)) == s:
            return True
        else:
            return False


print(is_palindrome([1, 2, 3, 2, 1]))
print(type([1, 2, 3]))
print(list(x for x in [1, 2, 3]))
print(list(x for x in reversed([1, 2, 3])))