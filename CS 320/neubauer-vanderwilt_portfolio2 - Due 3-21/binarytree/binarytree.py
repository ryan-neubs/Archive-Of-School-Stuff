# binarytree.py
# By Ryan Neubauer and Jacob Vanderwilt
# Binary tree class to use for binary tree algs

class BinaryTree:
    def __init__(self, vertices, root):
        self.children = {v:[None,None] for v in vertices}
        self.root = root
    
    def addchild(self, v, l, r):
        self.children[v][0] = l
        self.children[v][1] = r

    def getleft(self, v):
        return self.children[v][0]

    def getright(self, v):
        return self.children[v][1]

    def hasleft(self, v):
        if self.children[v][0] != None:
            return True
        return False

    def hasright(self, v):
        if self.children[v][1] != None:
            return True
        return False

    def vertex_iter(self):
        return iter(self.children.keys())

    def children_iter(self):
        return iter(self.children_values())

def fromfile(file):
    with open(file) as f:
        v = f.readline().strip().split()
        r = f.readline().strip()
        bt = BinaryTree(v,r)
        for line in f:
            v, l, r = line.strip().split()
            if l == 'None':
                l = None
            if r == 'None':
                r = None
            bt.addchild(v, l, r)
    return bt