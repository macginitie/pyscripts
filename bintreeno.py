#!/usr/bin/python

# note from polycopter: can't recall where I found this code originally
# I added "contains()" and "delete()" and removed 'object' inheritance

class Node():

    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.keycount = 1 # this is nonstandard, eh? I think so


class BinaryTree():

    def __init__(self, key):
        self.root = Node(key)

    def add(self, key):
        nd = self.root
        while nd is not None:
            saved_place = nd
            if nd.key > key:
                nd = nd.left
            elif nd.key == key:
                nd.keycount += 1 # nonstandard?
                return
            else:
                nd = nd.right
        if saved_place.key > key:
            saved_place.left = Node(key, saved_place)
        else:
            saved_place.right = Node(key, saved_place)

    def traverse(self, nd, func):
        if nd.left is not None:
            self.traverse(nd.left, func)
        for i in range(nd.keycount):
            func(nd.key)
        if nd.right is not None:
            self.traverse(nd.right, func)

    def printTree(self):
        self.traverse(self.root, print)

    def traverseDbg(self, nd, func):
        if nd.left is not None:
            self.traverseDbg(nd.left, func)
        for i in range(nd.keycount):
            if nd.parent is not None:
                func(nd.key, nd.parent.key)
            else:
                func(nd.key, 'None')
        if nd.right is not None:
            self.traverseDbg(nd.right, func)

    def debugPrint(self):
        self.traverseDbg(self.root, print)

    def contains(self, key):
        nd = self.root
        while nd is not None:
            if nd.key > key:
                nd = nd.left
            elif nd.key == key:
                return True
            else:
                nd = nd.right
        return False

    def smallestKey(self, nd):
        if nd is not None:
            if nd.left is not None:
                return self.smallestKey(nd.left)
            else:
                return nd.key
        else:
            # TO DO: should raise exception here
            return None

    def delete(self, key):
        nd = self.root
        side = '?'
        while nd is not None:
            if nd.key > key:
                side = 'L'
                nd = nd.left
            elif nd.key == key:
                nd.keycount -= 1 # keycount always starts at 1, in Node() ctor
                if nd.keycount == 0:
                    # handle 3 cases to delete node nd
                    if nd.left is None:
                        if nd.right is None:
                            # case 1: no children, just delete this node
                            if side == 'L':
                                nd.parent.left = None
                            elif side == 'R':
                                nd.parent.right = None
                        else:
                            # case 2a: connect right child to parent
                            # & connect parent to right child
                            if side == 'L':
                                nd.parent.left = nd.right
                            elif side == 'R':
                                nd.parent.right = nd.right
                            nd.right.parent = nd.parent
                    elif nd.right is None:
                        # case 2b: connect left child to parent
                        # & connect parent to left child
                        if side == 'L':
                            nd.parent.left = nd.left
                        elif side == 'R':
                            nd.parent.right = nd.left
                        nd.left.parent = nd.parent
                    else:
                        # case 3:
                        swapkey = self.smallestKey(nd.right)
                        # 'catch' exception
                        if swapkey is None:
                            print('ERROR: smallestKey() failed')
                            return
                        self.delete(swapkey)
                        nd.key = swapkey
                # all done if we get here
                return
            else:
                side = 'R'
                nd = nd.right


if __name__ == '__main__':
    testTree = BinaryTree('p')
    for c in 'olycopter': testTree.add(c)
    testTree.printTree()
    testTree.debugPrint()

    piTree = BinaryTree(3)
    for d in [1,4,1,5,9]: piTree.add(d)
    piTree.printTree()
    piTree.debugPrint()

    print(testTree.contains('p'), testTree.contains('x'))
    print(piTree.contains(1), piTree.contains(8))

    testTree.delete('y')
    testTree.printTree()
    testTree.debugPrint()
    testTree.add('x')
    testTree.debugPrint()
    testTree.delete('t')
    testTree.debugPrint()

    piTree.delete(9)
    piTree.printTree()
    piTree.debugPrint()
