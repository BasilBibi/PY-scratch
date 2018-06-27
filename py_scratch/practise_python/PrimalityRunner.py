from py_scratch.practise_python.Primality import *

while True:
    try:
        n=int(input('\nPlease enter an integer to test for primality: '))
        if is_prime(n):
            print(f'{n} is a prime number')
        else:
            print(f'{n} is NOT prime number')
    except ValueError as verr:
        print(verr)
