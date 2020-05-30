import os
from os.path import join
import sys

def walk_dir_tree( starting_folder, target_ext_list ):
    for root, dirs, files in os.walk( starting_folder ):
        for name in files:
            fqpn = join( root, name )
            for ext in target_ext_list:
                if ext == name[-len(ext):]: print( 'del "' + fqpn + '"' )
            
if __name__ == '__main__':
    root = '.'
    try:
        root = sys.argv[1]
    except:
        pass
    extlist0 = ['sdf', 'suo', 'obj', 'sbr', 'pch', 'exe', 'dll', 'ilk', 'pdb', 'scc', 'idb', 'exp', 'lib', 'bsc', 'plg', 'res', 'opt', 'rig', 'log', 'ncb' ]
    extlist = []
    for x in extlist0: extlist.append( '.' + x )
    extlist2 = [ '.manifest', '.lastbuildstate', '_manifest.rc', '.cache', '.opensdf', '.user', '.ipch', '.tlog' ]
    for y in extlist2: extlist.append( y )
    print( 'rem --------' )
    print( 'rem', extlist )
    print( 'rem --------' )
    walk_dir_tree( '.', extlist )