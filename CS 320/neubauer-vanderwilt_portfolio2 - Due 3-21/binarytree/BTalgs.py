# BTalgs.py
# By Ryan Neubauer
# Inorder, preorder, and postorder BT traversals

from binarytree import *

def inorder(tree, v, path=[]):
    path = path
    if tree.hasleft(v): inorder(tree, tree.getleft(v), path)
    path.append(v)
    if tree.hasright(v): inorder(tree, tree.getright(v), path)
    return path

def preorder(tree, v, path=[]):
    path = path
    path.append(v)
    if tree.hasleft(v): preorder(tree, tree.getleft(v), path)
    if tree.hasright(v): preorder(tree, tree.getright(v), path)
    return path

def postorder(tree, v, path=[]):  # DOES NOT WORK - DIDN'T GET TIME TO TWEAK
    path = path
    if tree.hasleft(v): preorder(tree, tree.getleft(v), path)
    if tree.hasright(v): preorder(tree, tree.getright(v), path)
    path.append(v)
    return path