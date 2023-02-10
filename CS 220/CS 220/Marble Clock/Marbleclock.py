#Marbleclock.py

from IterableQueue import *
from BoundedStack import *

class Marbleclock:

    def __init__(self, traylimits = [4, 11, 11], n = 27):
        self.reservoir = IterableQueue()
        self.og_order = []
        self.marbles = n
        for marble in range(n):
            self.og_order.append(marble + 1)
            self.reservoir.enqueue(marble + 1)

    def drop_marble(self):
        pass

    def isFull(self, traylimit):
        pass
    
    def run_cycle(self):
        pass

    def inorder(self):
        curr_order = []
        iterate = iter(self.reservoir)
        for marble in range(self.marbles):
            
