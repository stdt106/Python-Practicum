def to_string(*d, sep=' ', end='\n'):
    return sep.join(str(x) for x in d) + end