#!/usr/bin/python

class Node(object):
    
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.keycount = 1
        

class BinaryTree(object):

    def __init__(self, key):
        self.root = Node(key)
        
    def add(self, key):
        nd = self.root
        while (nd is not None):
            saved_place = nd
            if (nd.key > key):
                nd = nd.left
            elif (nd.key == key):
                nd.keycount += 1
                return
            else:
                nd = nd.right
        if saved_place.key > key:
            saved_place.left = Node(key, saved_place)
        else:
            saved_place.right = Node(key, saved_place)
            
    def traverse(self, nd, func):
        if (nd.left is not None):
            self.traverse(nd.left, func)
        for i in range(nd.keycount):
            func(nd.key)
        if (nd.right is not None):
            self.traverse(nd.right, func)
            
    def printTree(self):
        self.traverse(self.root, print)
            
if __name__ == '__main__':
    testTree = BinaryTree('p')
    testTree.add('o')
    testTree.add('l')
    testTree.add('y')
    testTree.add('c')
    testTree.add('o')
    testTree.add('p')
    testTree.add('t')
    testTree.add('e')
    testTree.add('r')
    testTree.printTree()

