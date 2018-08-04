def fact(n):
    if n <= 0:
        return 0
    else:
        accumulator = 1
        while n > 0:
            accumulator = accumulator * n
            n = n - 1
        return accumulator
