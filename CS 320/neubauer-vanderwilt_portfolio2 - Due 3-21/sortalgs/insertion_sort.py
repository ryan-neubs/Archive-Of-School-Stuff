# insertion_sort.py
# By Ryan Neubauer and Jacob Vanderwilt

def insertion_sort(lst):
    for i in range(len(lst)):
        v = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > v:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = v

def main():
    lst = [2, 3, 1, 5, 7, 4, 12, 10, 9]
    insertion_sort(lst)
    print(lst)

main()
