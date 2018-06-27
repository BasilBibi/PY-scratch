def is_prime(n):
    if n < 2 :
        return False
    if n == 2 or n == 3:
        return True
    # Can use bitwise operator to check if even
    # if n & 1 == 0:
    if n % 2 == 0:
        return False
    for e in range(5, n):
        if n % e == 0:
            print(f'Not prime {n}/{e} = 0')
            return False
    return True
