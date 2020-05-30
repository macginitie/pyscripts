#usr/bin/python

import os
from os.path import join, getsize
import sys

def checksizes(path) :
	print(path)
	for root, dirs, files in os.walk(path):
		print( root, "consumes \t\t", end="")
		print( sum(getsize(join(root, name)) for name in files) )
		
if __name__ == "__main__" :
	if len(sys.argv) > 1 :
		#for arg in sys.argv :
		#	print(arg)
		checksizes(sys.argv[1])
	else :
		print('a primitive version of the Unix "du" utility')
		print('usage: python unix-du.py path')
	