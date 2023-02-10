# tri_area.py
# by Ryan Neubauer

import math

def compute_area(a, b, c):
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    a = int(input("Enter the first side length: "))
    b = int(input("Enter the second side length: "))
    c = int(input("Enter the third side length: "))
    print("The are of the triangle is:", compute_area(a, b, c))
    
main()
