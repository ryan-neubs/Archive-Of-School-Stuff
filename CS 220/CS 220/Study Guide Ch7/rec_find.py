def rec_find(self, item):
    self.root = self._findNode(self.root, item)

def _findNode(self, root, item):
    if root.item == item:
        return root

    if root.item < item:
        root.left = self._findNode(root.left, item)
    else:
        root.item = self._findNode(root.right, item)
