# lightning.py
# A program to tell you how far away a storm is
# by: Ryan Neubauer

def lightning():
    print("This program will tell you how far away a storm is.")
    seconds = eval(input("How many seconds were between lightning and thunder? Enter a value: "))
    distance = (1100 * seconds)/5280
    print("The storm is", distance, "miles away.")
    input("Press <Enter> to quit.")

lightning()
