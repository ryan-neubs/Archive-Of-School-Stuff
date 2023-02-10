# subsets.py
# by Ryan Neubauer and Jacob Vanderwilt

def subsets_bu(lst):
    result = [[]]
    for i in range(len(lst)):
        result += [item + [lst[i]] for item in result]
    return result

def subsets_td(lst):
    if len(lst) == 0:
        return [[]]
    res = subsets_td(lst[:-1])
    return res + [item + [lst[-1]] for item in res]




