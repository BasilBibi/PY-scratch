def get_list_overlap(a, b):
    result = set()
    for e in b:
        if e in a and e not in result:
            result.add(e)

    return result


def list_intersection(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a.intersection(set_b)


def list_intersection_with_ampersand(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a & set_b


def list_union(a, b):
    return set(a).union(set(b))


def list_difference(a, b):
    return set(a).difference(set(b))


def list_sym_diff(a, b):
    return set(a).symmetric_difference(set(b))
