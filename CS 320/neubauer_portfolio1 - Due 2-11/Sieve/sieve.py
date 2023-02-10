# sieve.py
# by Ryan Neubauer
# This program represents the Sieve of Eratosthenes algorithm in Python

import math

def sieve(n):
    assert n > 1
    A = [0,0] # Added two zeros so the algorithm could work with zero based indexing
    for p in range(2,n+1):
        A.append(p)
    for p in range(2,math.floor(math.sqrt(n))+1):
        if A[p] != 0:
            j = p * p
            while j <= n:
                A[j] = 0
                j = j + p

    L = []
    for p in range(2,n):
        if A[p] != 0:
            L.append(A[p])
    return L

def main():
    print("This program demonstrates the Sieve of Eratosthenes algorithm")
    while True:
        n = input("Please enter a value greater than 1 (Press <Enter> to quit): ")
        if n == '':
            quit()
        print("\nYou entered:", n,"\nYour output is:")
        print(sieve(int(n)),"\n")

if __name__ == "__main__":
    main()