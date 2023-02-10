# chaos.py
# by Ryan Neubauer

def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(1000):
        x = 3.9 * x * (1-x)
        print(x)

main()
