# RandomList.py
from random import randint

def randomListGenerator():
    A = []
    for i in range(randint(3,100)):
        A.append(randint(0,100))
    return A