#usr/bin/python

import os
from os.path import join
import sys
import time


def checkdate(path) :
	l8st = 0
	print(path)
	for root, dirs, files in os.walk(path):
		for name in files:
			statobj = os.lstat(join(root, name))
			if statobj.st_mtime > l8st:
				l8st = statobj.st_mtime				
	modtime2 = time.localtime(l8st)
	modtime = time.strftime("%m/%d/%Y %H:%M:%S", modtime2)
	print('no files newer than ', modtime)


if __name__ == "__main__" :
	if len(sys.argv[0]) > 0 :
		# for arg in sys.argv :
		#     print(arg)
		checkdate(sys.argv[1])
	else:
		print('usage: python checkd8.py path')
