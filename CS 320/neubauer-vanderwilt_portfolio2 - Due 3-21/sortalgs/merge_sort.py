# merge_sort.py
# By Ryan Neubauer and Jacob Vanderwilt

def merge_sort(a):
    if len(a) <= 1:
        return a
    b = a[:len(a)//2]
    c = a[len(a)//2:]
    b = merge_sort(b)
    c = merge_sort(c)
    z = merge(b, c)
    return z

def merge(b, c):
    i = 0
    j = 0
    a = []
    while i < len(b) and j < len(c):
        #print(f"{i} {p}, {j} {q}")
        if b[i] < c[j]:
            a.append(b[i])
            i += 1
        else:
            a.append(c[j])
            j += 1
    if i < len(b):
        for v in range(i, len(b)):
            a.append(b[v])
    else:
        for v in range(j, len(c)):
            a.append(c[v])
    return a

def main():
    lst = [8, 3, 2, 9, 7, 1, 5, 4]
    ans = merge_sort(lst)
    print(ans)
main()
