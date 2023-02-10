# fibfun.py

import functools
memoize = functools.lru_cache(maxsize=None)

@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_dpbu(n):
    table = [None] * (n+1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

class Fib_dptd:

    def __init__(self):
        self.table = {}

    def fib(self, n):
        if n in self.table:
            return self.table[n]

        if n == 0:
            return 0
        if n == 1:
            return 1
        ans = self.fib(n-1) + self.fib(n-2)
        self.table[n] = ans
        return ans
    
class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
    
