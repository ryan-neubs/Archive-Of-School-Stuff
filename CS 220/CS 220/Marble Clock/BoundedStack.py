#tray.py

class BoundedStack:
    def __init__(self, maxsize):
        self.items = []
        self.maxsize = maxsize

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        assert self.isFull() == False
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def isFull(self):
        return self.size() == self.maxsize

    def size(self):
        return len(self.items)


    
