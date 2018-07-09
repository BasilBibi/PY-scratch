def get_second_largest(l):
    if l is None or len(l) == 0:
        return None
    s = set(l)
    s.remove(max(s))
    if len(s) == 0:
        return None
    return max(s)
