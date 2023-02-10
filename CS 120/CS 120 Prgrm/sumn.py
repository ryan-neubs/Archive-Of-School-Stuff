#sumn.py
# by Ryan Neubauer


def sumN(n):
    # returns the sum of numbers from 1 through n
    total = 0
    for i in range(1, n + 1):
        total = i + total
        print(total)
    return total
    
def main():
    print("This program returns the sum of the natural")
    print("numbers from 1 to n.")
    last = int(input("\nEnter the value of n: "))
    print("The sum is:", sumN(last))
    
main()
          
