def common(lst1, lst2):
    commons = []
    for item in lst1:
        if item in lst2:
            commons.append(item)
            lst2.remove(item)
    return commons
