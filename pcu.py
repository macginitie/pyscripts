#!/usr/bin/python

# pcu : Path Clean Up, a script to gener8 .bat file commands to delete .pdb files
# and other unnecessary space hogs from throughout the subfolders of a given path

import os
from os.path import join
import sys
import time

def generate_del_commands( path ) :
    count = 0
    rejects = ['old', 'orig', 'obj', 'sbr', 'pch', 'exe', 'dll', 'ilk', 'pdb', 'scc', 'idb', 'exp', 'lib', 'bsc', 'plg', 'res', 'opt', 'rig', 'log', 'ncb', 'aps', 'clw']
    for root, dirs, files in os.walk(path) :
        for name in files :
            ext = name[-3:]
            if (ext in rejects):
                print( 'del "', join(root, name) )
                count += 1
    print( 'rem ', count, ' deleted.' )
            

if __name__ == "__main__" :
    
    if len( sys.argv ) > 1:
        generate_del_commands( sys.argv[1] )
    else :
        print( 'usage: python ' + sys.argv[0] + ' from_path' )
