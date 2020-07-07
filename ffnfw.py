#usr/bin/python

import os
from os.path import join, getsize
import sys

def fixnames(path) :
	print('modifying file names in {0}'.format(path))
	for root, dirs, files in os.walk(path):
        # 2DO
		print(join(root, name) for name in files)
		
if __name__ == "__main__" :
	if len(sys.argv) > 1 :
		fixnames(sys.argv[1])
	else :
		print('a utility to "fix" Linux file names that are invalid for Windows')
		print('usage: python ffnfw.py path')
        print('changes any names in path & its subfolders which contain ":" or "?"')
        print("maybe this goes without saying, but: it's pointless to run this in Windows")
	