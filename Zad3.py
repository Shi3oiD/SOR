def find_max(*args):
    if len(args) == 0:
        return None
    max_value = args[0]
    for value in args[1:]:
        if value > max_value:
            max_value = value
    print(max_value)
    return max_value
