from py_scratch.practise_python.Primality import *

while True:
    try:
        i = int(
            input('\nPlease enter an integer to test for primality: ')
        )
        if is_prime(i):
            print(f'{i} is a prime number')
        else:
            print(f'{i} is NOT prime number')
    except ValueError as verr:
        print(verr)
