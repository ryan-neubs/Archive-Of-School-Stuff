# pi.py
# this program estimates the digits of pi
# by Ryan Neubauer

import math

sgn = 1
total = 0

print("This program estimates the digits of pi.")
n = int(input("Enter a positive integer for n: "))
for denom in range(1,2*n,2):
    term = sgn*4/denom
    total = total + term
    sgn = sgn * (-1)
print("The estimate of pi is:", total)
print("The margin of error is:", total-math.pi)
    

