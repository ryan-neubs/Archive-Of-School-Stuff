# pizza.py
# This program calculates the cost per square inch of pizza
# by Ryan Neubauer

import math

def main():
    price = int(input("Enter the price of pizza in cents: "))
    diameter = float(input("Enter the diameter of the pizza in inches: "))
    print()
    
    area = math.pi * ((diameter/2) ** 2)
    costPerSquInch = price / area

    print()
    print("The cost per quare inch of pizza is", costPerSquInch, "cents per inch.")
    print()
    input("Press <Enter> to quit")

main()
