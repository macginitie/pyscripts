#!/usr/bin/python

import os
from os.path import join
import sys
import time


def checkdate(path, date):
    count = 0
    # print(path)
    rejects = ['sdf', 'suo', 'obj', 'sbr', 'pch', 'ilk', 'pdb', 'scc', 'idb', 'exp', 'lib', 'bsc', 'plg', 'res', 'opt',
               'rig', 'log', 'ncb', 'aps', 'clw']
    rejects2 = ['.manifest', '.lastbuildstate', '_manifest.rc', '.cache', '.opensdf', '.user']
    for root, dirs, files in os.walk(path):
        for name in files:
            ext = name[-3:]
            if not (ext in rejects):
                statobj = os.lstat(join(root, name))
                if statobj.st_mtime > date:
                    print('copy ', join(root, name))
                    count += 1
                    fullname = join(root, name)
                    ok = True
                    for rej in rejects2:
                        if rej in fullname:
                            ok = False
                            break
                    if ok:
                        print('copy ', fullname)
                        count += 1
    modtime2 = time.localtime(date)
    modtime = time.strftime("%m/%d/%Y %H:%M:%S", modtime2)
    print(count, ' files newer than ', modtime)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        # for arg in sys.argv:
        #   print(arg)
        checkdate(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) > 1:
        checkdate(sys.argv[1], 1447700000)  # 11/16/2015 13:53:20
        # note: 86400 seconds per day
    else:
        print('usage: python ' + sys.argv[0] + ' path [mtime]')
        statobj = os.lstat(sys.argv[0])
        print('os.lstat( ' + sys.argv[0] + ' ).st_mtime ==', statobj.st_mtime)
