def islower(c):
    if len(c) != 1:
        return False  # Not a single character
    return 'a' <= c <= 'z'
