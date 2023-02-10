def syracuse(num):
    if num % 2 == 0:
        return num//2
    else:
        return(num * 3) + 1

def create_sequence(start):
    # returns a list of numbers in syracuse seq with the given start
    seq = []
    num = start
    while num != 1:
        # update seq
        seq.append(num)
        num = syracuse(num)
    seq.append(num)
    return seq

def main():
    syrnum = int(input("Enter a number to start your pattern: "))
    while syrnum != 1:
        print(syracuse(syrnum))
        syrnum = syracuse(syrnum)
    print(syrnum)

if __name__ == "__main__":
    main()
    



