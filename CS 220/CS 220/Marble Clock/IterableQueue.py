#IterableQueue.py

class IterableQueue:
    
    class Node:

        def __init__(self, item = None):
            self.item = item
            self.link = None
        
    def __init__(self):
        self._front = None
        self._curr = None
        self._back = None
        self._size = 0

    def __iter__(self):
        self._curr = self._front
        return self

    def __next__(self):
        if self._curr != None:
            nextitem = self._curr.item
            self._curr = self._curr.link
            return nextitem

    def enqueue(self, newItem):
        _Node = self.Node(newItem)
        _Node.link = None
        if self._front is not None:
            self._back.link = _Node
        else:
            self._front = _Node
        self._back = _Node
        self._size += 1

    def dequeue(self):
        if self._front is not None:
            removedNode = self._front
            self._front = self._front.link
            self._size -= 1
        return removedNode.item

    def front(self):
        return self._front.item

    def size(self):
        return self._size
