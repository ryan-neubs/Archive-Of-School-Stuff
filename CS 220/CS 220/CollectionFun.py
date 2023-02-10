# By Ryan Neubauer, Gavin Roy, Tryton Harper, and Yohannes Dawit

'''Instructions:

Select a team spokesperson to fork this repl and share the join
link with your group.

For each method f1--f5 investigate the method by reading the code, 
tracing it by hand, and running some experiments. Once you have 
decided what the method does, do the following:

a) Choose an appropriate name for the method and "clean up" any
   variable names that you think could be improved.
b) Write a docstring for the method with a brief description and 
   appropriate pre and post conditions.
c) Give a theta analysis of the running time of the method as a 
   function of the len of self.items.

Rejoin the class after you have completed f1 and f2.
'''

from random import randrange

class CollectionFun:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items[:]

    def item_swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def scramble_500(self):
      '''Scrambles random spots in the list 500 times
      pre: items within list can be swapped
      post: List swaps random items 500 times
      '''
      for _ in range(500):
          ri1 = randrange(self.size())
          ri2 = randrange(self.size())
          self.item_swap(ri1, ri2)
#Theta(1)

    def self_scramble(self):
      ''' Scrambles based on the location of i and the size of the list.'''
      for i in range(self.size()):
          ri = randrange(i, self.size())
          self.item_swap(i, ri)
#Theta(n)

    def f3(self, start):
      mi = start
      for i in range(start, self.size()):
          if self.items[i] < self.items[mi]:
              mi = i
      return mi

    def f4(self):
      for i in range(self.size()):
          mi = self.f3(i)
          self.item_swap(i, mi)

    def f5(self):
      self.f4()
      uitems = [self.items[0]]
      for item in self.items:
          if item != uitems[-1]:
              uitems.append(item)
      return uitems


def build():
    c = CollectionFun()
    for i in [3,1,4,1,5,9,2,6,5]:
        c.add(i)
    return c

