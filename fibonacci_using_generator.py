"""
Fibonacci series:
It's a sequence where each number is the sum of the two preceding ones, starting from 0 and 1.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b,a+b

f1 = fibonacci()

assert(next(f1) == 0)
assert(next(f1) == 1)
assert(next(f1) == 1)
assert(next(f1) == 2)
assert(next(f1) == 3)
assert(next(f1) == 5)
assert(next(f1) == 8)