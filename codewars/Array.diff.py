def array_diff(a, b):
    new_list = [x for x in a if x not in b]
    return new_list