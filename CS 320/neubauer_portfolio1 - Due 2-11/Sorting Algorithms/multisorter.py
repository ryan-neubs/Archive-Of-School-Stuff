# multisorter.py
# By Ryan Neubauer
# Program to compare different sorting algorithms

from BubbleSort import BubbleSort
from CompareCountSort import CompareCountSort
from SelectionSort import SelectionSort
from random import randint
import time

def main():
    print("Welcome to the mutlisorter")
    print("Choose which algorithms you'd like to use: ")
    print("1: Bubble Sort \n2: Compare Count Sort \n3: Selection Sort")
    selection = input("Enter your selections separated by spaces and press enter: ").split()
    selection = [int(i) for i in selection]
    size = int(input("Enter test list size: "))
    min, max = input("Enter a value range (ex. 0 100): ").split()
    trials = int(input("Enter emount of trials for each algorithm: "))

    A = []
    averages = []
    for i in range(size):
        A.append(randint(int(min), int(max)))
    
    if 1 in selection:
        # Bubble Sort
        print("Starting Bubble Sort...\n")
        BubbleAvg = []
        for i in range(trials):
            start = time.time()
            BubbleSort(A)
            end = time.time()
            elapsed = end - start
            BubbleAvg.append(elapsed)
            print(f"Trial {i+1}: ", elapsed, "\n")
        BubbleTime = sum(BubbleAvg)/len(BubbleAvg)
        averages.append("Bubble: " + str(BubbleTime))

    if 2 in selection:
        # Compare Count Sort
        print("Starting Compare Count Sort...\n")
        CompareCountAvg = []
        for i in range(trials):
            start = time.time()
            CompareCountSort(A)
            end = time.time()
            elapsed = end - start
            CompareCountAvg.append(elapsed)
            print(f"Trial {i+1}: ", elapsed, "\n")
        CompareCountTime = sum(CompareCountAvg)/len(CompareCountAvg)
        averages.append("Compare Count: " + str(CompareCountTime))

    if 3 in selection:
        # Selection Sort
        print("Starting Selection Sort...\n")
        SelectionAvg = []
        for i in range(trials):
            start = time.time()
            SelectionSort(A)
            end = time.time()
            elapsed = end - start
            SelectionAvg.append(elapsed)
            print(f"Trial {i+1}: ", elapsed, "\n")
        SelectionTime = sum(SelectionAvg)/len(SelectionAvg)
        averages.append("Selection Sort: " + str(SelectionTime))

    print("Average Times:")
    for item in averages:
        print(item)


if __name__ == "__main__":
    main()