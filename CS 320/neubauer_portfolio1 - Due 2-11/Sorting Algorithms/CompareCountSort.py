#CompareCountSort.py
from random import randint
import time

def CompareCountSort(A):
    # Algorithm body
    Count = []
    S = []
    for i in range(len(A)):
        Count.append(0)
        S.append(0)
    for i in range(len(A)-1):
        for j in range(i + 1, len(A)):
            if A[i] < A[j]:
                Count[j] = Count[j] + 1
            else:
                Count[i] = Count[i] + 1
    for i in range(len(A)):
        S[Count[i]] = A[i]
    return S

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
        CompareCountSort(A)
        end = time.time()
        elapsed_time = end - start
        print(f"\nTrial {trial+1}: ", elapsed_time)
        times.append(elapsed_time)

    print("\nAverage time: ", sum(times)/len(times))
    input("\nPress [Enter] to quit.")


if __name__ == '__main__':
    main()