import math
from functools import lru_cache
from utils.time_measuring import measured_time


# A most naive and hard-coded algorithm with full recursive
def fibonachi_recursive(n):
    return n if n < 2 else fibonachi_recursive(n - 2) + fibonachi_recursive(n - 1)


# Memoized algorithm
memo = {0: 0, 1: 1}


def fibonachi_memoized(n):
    if n not in memo:
        memo[n] = fibonachi_memoized(n - 1) + fibonachi_memoized(n - 2)
    return memo[n]


# Auto-memoized algorithm
@lru_cache(maxsize=None)
def fibonachi_lru(n):
    return n if n < 2 else fibonachi_lru(n - 2) + fibonachi_lru(n - 1)


# Fastest algorithm on iteration instead of recursive
@measured_time
def fibonachi_loop(n):
    if n == 0:
        return 0
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


# Generator of fibonachi numbers
def fibonachi_generator(n):
    yield 0
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


# Algorithm with Binet's formula
@measured_time
def fibonachi_binet(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return int(phi ** n / sqrt5 + 0.5)


def main():
    print(fibonachi_lru(500))
    print(fibonachi_memoized(500))
    print(fibonachi_loop(500))
    print(fibonachi_binet(500))
    print(fibonachi_recursive(500))


if __name__ == "__main__":
    main()
