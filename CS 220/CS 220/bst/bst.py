# bst.py
#   Stripped-down binary search tree
# by Ryan Neubauer and Gavin Roy


class TreeNode(object):

    def __init__(self, data = None, left=None, right=None):
    
        """creates a tree node with specified data and references to left 
        and right children"""
    
        self.item = data
        self.left = left
        self.right = right
        self.count = 1



class MultiSet:

    #------------------------------------------------------------

    def __init__(self):
        
        """create empty binary search tree
        post: empty tree created"""

        self.root = None

    #------------------------------------------------------------

    def insert(self, item):

        """insert item into binary search tree
        pre: item is not in self
        post: item has been added to self"""

        self.root = self._subtreeInsert(self.root, item)

    #------------------------------------------------------------

    def _subtreeInsert(self, root, item):

        if root is None:          # inserting into empty tree
            return TreeNode(item) # the item becomes the new tree root

        if item == root.item:
            root.count += 1

        if item < root.item:                              # modify left subtree
            root.left = self._subtreeInsert(root.left, item)
        else:                                             # modify right subtree 
            root.right = self._subtreeInsert(root.right, item)

        return root # original root is root of modified tree

    #------------------------------------------------------------

    def find(self, item):
        
        """ Search for item in BST
            post: Returns item from BST if found, None otherwise"""

        node = self.root
        while node is not None and node.item != item:
            if item < node.item:
                node = node.left
            else:
                node = node.right

        if node is None:
            return 0
        else:
            return node.count

    #------------------------------------------------------------

    def delete(self, item):

        """remove item from binary search tree
        post: item is removed from the tree"""
        
        self.root = self._subtreeDelete(self.root, item)
        self.root.count =- 1

    #------------------------------------------------------------

    def _subtreeDelete(self, root, item):

        if root is None:   # Empty tree, nothing to do
           return None
        if item < root.item:                             # modify left
            root.left = self._subtreeDelete(root.left, item)
        elif item > root.item:                           # modify right
            root.right = self._subtreeDelete(root.right, item)
        else:                                            # delete root
            if root.left is None:                        # promote right subtree
                root =  root.right
            elif root.right is None:                     # promote left subtree
                root = root.left
            else:
                # root node can't be deleted, overwrite it with max of 
                #    left subtree and delete max node from the subtree
                root.item, root.left = self._subtreeDelMax(root.left)
        return root

    #------------------------------------------------------------

    def _subtreeDelMax(self, root):
        
        if root.right is None:           # root is the max 
            return root.item, root.left  # return max and promote left subtree
        else:
            # max is in right subtree, recursively find and delete it
            maxVal, root.right = self._subtreeDelMax(root.right)
            return maxVal, root  

    #------------------------------------------------------------

    def __iter__(self):

        """in-order iterator for binary search tree"""
        
        return self._inorderGen(self.root)

    #------------------------------------------------------------

    def _inorderGen(self, root):
        
        if root is not None:
            # yield all the items in the left subtree
            for item in self._inorderGen(root.left):
                yield item
            yield root.item
            # yield all the items from the right subtree
            for item in self._inorderGen(root.right):
                yield item
    #------------------------------------------------------------
def treeSort(lst):
    tree = MultiSet()
    for item in lst:
        tree.insert(item)
    lst = list(tree)
    return lst
        
if __name__ == "__main__":

    print("Part 0 Tests:", end=" ")
    test = MultiSet()
    test.insert(5)
    test.insert(3)
    test.insert(7)
    assert test.root.item == 5
    assert test.root.left.item == 3
    assert test.root.right.item == 7
    assert list(test) == [3,5,7]
    print("OK")

    print("Part 1 Tests:", end=" ")
    n = TreeNode(4)
    assert n.count == 1
    n = TreeNode("Hello", None, None)
    assert n.count == 1
    assert test.root.count == 1
    assert test.root.left.count == 1
    assert test.root.right.count == 1
    print("OK")
    
    print("Part 2 Tests:", end=" ")
    test.insert(5)
    assert test.root.count == 2
    test.insert(3)
    assert test.root.left.count == 2
    test.insert(3)
    assert test.root.left.count == 3
    assert test.root.count == 2
    assert test.root.right.count == 1
    test.insert(6)
    assert test.root.right.left.count == 1
    test.insert(7)
    assert test.root.right.count == 2
    print("OK")
    
    print("Part 3 Tests:", end=" ")
    assert list(test) == [3,3,3,5,5,6,7,7]
    print("OK")
    
    print("Part 4 Tests:", end=" ")
    assert test.find(3) == 3
    assert test.find(5) == 2
    assert test.find(6) == 1
    assert test.find(7) == 2
    assert test.find(42) == 0
    print("OK")

    print("Part 5 Tests:", end=" ")
    test.delete(5)
    assert test.find(5) == 1
    test.delete(7)
    test.delete(7)
    test.delete(3)
    assert list(test) == [3,3,5,6]
    print("OK")

    print("Part 6 Tests:", end=" ")
    lst = [3,1,4,1,5,2,6,5,3,5]
    lst = treeSort(lst)
    assert lst == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6]
    print("OK")
