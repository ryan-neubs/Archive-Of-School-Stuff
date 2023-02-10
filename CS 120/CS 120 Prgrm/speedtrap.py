# speedtrap.py
# by Ryan Neubauer
# This program calculates speeding tickets for Podunksville

def calculate_fine(speed, speedlimit):

    speed_dif = speed - speedlimit

    if speed_dif > 0:
        if speed > 90:
            ticket = 50 + (speed_dif * 5) + 200

        else:
            ticket = 50 + (speed_dif * 5)
        
        print(" ")
        print("Tsk tsk, you were above the legal speed. Your ticket is", ticket, "dollars.")

    else:
        print(" ")
        print("You were going a legal speed. Carry on")

def main():
    print("This program calculates your speeding ticket in Podunksville. \n")

    speedlim = int(input("Enter the speed limit: "))
    speed = int(input("Enter your clocked speed: "))

    calculate_fine(speed, speedlim)
    input("\nPress <Enter> to quit.")

if __name__ == "__main__":
    main()
    
