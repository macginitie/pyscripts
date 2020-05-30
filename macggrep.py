#!/usr/bin/env python3

import os
from os.path import join, getsize
import sys


def grep_cpp_files(path, pattern, debug):
    print('recursively looking for', pattern, 'in', path)
    for root, dirs, files in os.walk(path):
        if debug:
            print('looking in %s' % root)
        for fname in files:
            if fname[-4:] == '.cpp' or fname[-2:] == '.h':
                fullname = join(root, fname)
                lines = open(fullname).readlines()
                lcount = 0
                for line in lines:
                    lcount += 1
                    if pattern in line:
                        print(lcount, fullname, line[:-1])
        
        
if __name__ == "__main__":

    print('I got %s args' % len(sys.argv))
    for arg in sys.argv:
        print(arg)
        
    if len(sys.argv) > 2:
        # for arg in sys.argv:
        #    print(arg)
        if len(sys.argv) > 3:
            grep_cpp_files(sys.argv[1], sys.argv[2], True)
        else:
            grep_cpp_files(sys.argv[1], sys.argv[2], False)
    else:
        print('a specialized .cpp/.h files grep utility')
        print('usage: python macggrep.py path pattern')
