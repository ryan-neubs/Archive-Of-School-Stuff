#euclidean.py
import time

def gcd(m,n):
    while n != 0:
        m, n = n, m % n
    return m
