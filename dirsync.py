#! /usr/bin/python

from filecmp import dircmp

def print_diff_files( dcmp, which, ignore ):
    for name in dcmp.diff_files:
        if not (name[-4:] in ignore) :
            if (which == 'right') :
                print( "%s\%s" % (dcmp.right, name) )
            else :
                print( "%s\%s" % (dcmp.left, name) )
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files( sub_dcmp, which, ignore )

def print_rightonly_files( dcmp, ignore ):
    for name in dcmp.right_only:
        if not (name[-4:] in ignore) :
            print( "%s\%s" % (dcmp.right, name) )
    for sub_dcmp in dcmp.subdirs.values():
        print_rightonly_files( sub_dcmp, ignore )

        
if __name__ == '__main__' :        
    print( 'a script to compare 2 directory trees' )
    ignore = ['Release', 'Debug', 'DEBUG', 'RELEASE', 'vssver.scc', 'mssccprj.scc']
    ignore2 = ['.dsw', '.dsp', '.ncb', '.plg', '.exe']
    try :
        leftdir = sys.argv[1]
    except :
        leftdir = 'd:/src/py/picmerj/images/new'
    try :
        rightdir = sys.argv[2]
    except :
        rightdir = 'c:/Pictures'

    print( 'left:', leftdir )
    print( 'right:', rightdir )
    dcmp = dircmp( leftdir, rightdir, ignore )
    #dcmp.report_full_closure()

    print_diff_files( dcmp, 'right', ignore2 )
    print( '------------------------' )
    print_rightonly_files( dcmp, ignore2 )
