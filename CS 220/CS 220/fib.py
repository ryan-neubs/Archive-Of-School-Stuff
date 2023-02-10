# fib.py
def loopFib(n):
    # pre: n > 0
    # returns the nth Fibonacci number

    curr = 1
    prev = 1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    return curr

def recFib(n):
    if n < 3:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)
    
def fib3(n, curr=1, prev=1):
    if n <= 2:
        return curr
    else:
        return fib3(n-1, curr+prev, curr)
