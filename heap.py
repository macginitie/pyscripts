#!/usr/bin/python

class Heap(object):
    
    def __init__(self):
        self.root = 1
        self.keys = [0] # 0th element unused
        
    def add(self, key):
        self.keys.append(key)
        self.siftup()
        
    def siftup(self):
        newest = len(self.keys) - 1
        if newest > 1:
            parent = newest//2
            while parent > 0 and self.keys[parent] > self.keys[newest]:
                # swap
                self.keys[parent], self.keys[newest] = self.keys[newest], self.keys[parent]
                # move up a level
                newest = parent
                parent = parent//2
                
    def remove_min_key(self):
        retval, self.keys[self.root] = self.keys[self.root], self.keys[-1]
        # fix the heap
        self.keys = self.keys[:-1]
        self.siftdown()
        return retval

    def siftdown(self):
        top = self.root
        while top < len(self.keys):
            # check left child
            child = top*2
            rchild = child + 1
            if (child >= len(self.keys)):
                # done
                break
            if (rchild < len(self.keys)):
                if self.keys[child] > self.keys[rchild]:
                    child = rchild
            if self.keys[top] > self.keys[child]:
                # swap
                self.keys[top], self.keys[child] = self.keys[child], self.keys[top]
            top = child
            
    def debug(self):
        print(self.keys)

if __name__ == '__main__':
    testHeap = Heap()
    testHeap.add('p')
    testHeap.add('o')
    testHeap.add('l')
    testHeap.add('y')
    testHeap.add('c')
    testHeap.add('o')
    testHeap.add('p')
    testHeap.add('t')
    testHeap.add('e')
    testHeap.add('r')
    testHeap.debug()
