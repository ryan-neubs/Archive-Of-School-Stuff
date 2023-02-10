def printdata(self, root):
    #inorder traversal (left, root, right)
    lst = []
    if root:
        lst = self.inorderTraversal(root.left)
        res.append(root.data)
        lst = lst + self.inorderTraversal(root.right)
