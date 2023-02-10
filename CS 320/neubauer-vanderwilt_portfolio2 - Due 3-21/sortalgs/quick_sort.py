# quick_sort.py
# By Ryan Neubauer and Jacob Vanderwilt

def quicksort(a):
    helperqs(a, 0, len(a)-1)

def helperqs(a, l, r):
    if l < r:
        s = HoarePartition(a, l, r)
        helperqs(a, l, s - 1)
        helperqs(a, s + 1, r)

def HoarePartition(a, l, r):
    z = [a[l], a[(l + r)//2], a[r]]
    z.sort()
    a[l], a[(l + r)//2], a[r] = z[1], z[0], z[2]
    p = a[l]
    i = l
    j = r + 1

    while True:
        while True:
            i += 1
            if a[i] >= p:
                break
        while True:
            j -= 1
            if a[j] <= p:
                break
        a[i], a[j] = a[j], a[i]
        if i >= j:
            break
    a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def main():
    lst = [5, 3, 1, 9, 8, 2, 4, 7]
    quicksort(lst)
    print(lst)

main()
