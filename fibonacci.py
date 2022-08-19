import time
from math import sqrt


# Fibonacci solutions
fib_mem_cache = {0: 0, 1: 1}


def fib(n: int) -> int:
    """ Recursion fibonacci. Complexity: O(2^n) """
    return n if n in [0, 1] else fib(n-1) + fib(n-2)


def fib_mem(n: int) -> int:
    """ Memorizing fibonacci. Complexity: O(n) """
    if n in fib_mem_cache:
        return n

    fib_mem_cache[n] = fib(n-1) + fib(n-2)

    return fib_mem_cache[n]


def fib_iter(n: int) -> int:
    """ Iterative fibonacci. Complexity: O(n) """
    if n in [0, 1]:
        return n

    previous, fib_number = 0, 1

    for i in range(2, n+1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


def fib_negative(n: int) -> int:
    """ Negative fibonacci. Complexity: O(n) """
    if n == 0:
        return 0

    negative = n < 1 and n % 2 == 0

    return - fib_negative(abs(n) if negative else fib_negative(n))


def fib_golden_ratio(n: int) -> int:
    """ Golden ration fibonacci """
    f = 1.618034
    return int((f**n - (1-f)**n) / sqrt(5))


if __name__ == '__main__':
    start = time.perf_counter()
    print('Recursion. Fibonacci number is: %s' % fib(30))  # Don't pass big numbers :)
    print(time.perf_counter() - start)
    start = time.perf_counter()
    print('Memorizing. Fibonacci number is: %s' % fib_mem(30))
    print(time.perf_counter() - start)
    start = time.perf_counter()
    print('Iterative. Fibonacci number is: %s' % fib_iter(30))
    print(time.perf_counter() - start)
    start = time.perf_counter()
    print('Negative. Fibonacci number is: %s' % fib_iter(30))
    print(time.perf_counter() - start)
    start = time.perf_counter()
    print('Golden ratio. Fibonacci number is: %s' % fib_golden_ratio(30))
    print(time.perf_counter() - start)
