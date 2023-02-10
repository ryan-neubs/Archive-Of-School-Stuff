# sqeeze.py

def squeezebf(items):
    A = sorted(items)
    squoze = []
    for item in items:
        if item not in squoze:
            squoze.append(item)
    return squoze

def squeeze(items):
    
