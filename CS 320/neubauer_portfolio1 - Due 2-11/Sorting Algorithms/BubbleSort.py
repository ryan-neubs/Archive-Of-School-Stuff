# BubbleSort.py

from random import randint
import time

def BubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]

def main():
    # Getting user input for generating the list and trials

    n = int(input("Enter the length of the list you would like: "))
    min, max = input("Enter the range of values in the list (example: 0-100 will be 0 100): ").split()
    trials = int(input("Enter the amount of trials: "))
    
    times = []
    for trial in range(trials):
        A = []
        for i in range(n):
            A.append(randint(int(min), int(max)))
        
        start = time.time()
        BubbleSort(A)
        end = time.time()
        elapsed_time = end - start
        print(f"\nTrial {trial+1}: ", elapsed_time)
        times.append(elapsed_time)

    print("\nAverage time: ", sum(times)/len(times))
    input("\nPress [Enter] to quit.")


if __name__ == '__main__':
    main()