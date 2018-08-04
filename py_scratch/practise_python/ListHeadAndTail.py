def first_and_last_element(l):
    return [
        l[0], l[-1]
    ]


def head_and_tail(l):
    head, *tail = l
    return head, tail


def head_and_tail_slices(l):
    return l[0], l[1:]
