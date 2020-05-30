from filecmp import dircmp

def print_diff_files( dcmp, which, ignore ):
    for name in dcmp.diff_files:
        if not (name[-4:] in ignore) :
            if (which == 'right') :
                print( "%s\%s" % (dcmp.right, name) )
            else :
                print( "%s\%s" % (dcmp.left, name) )
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files( sub_dcmp, which )

def print_rightonly_files( dcmp, ignore ):
    for name in dcmp.right_only:
        if not (name[-4:] in ignore) :
            print( "%s\%s" % (dcmp.right, name) )
    for sub_dcmp in dcmp.subdirs.values():
        print_rightonly_files( sub_dcmp )

# the next 4 lines document what this script is for (to some extent, at least)
ignore = ['Release', 'Debug', 'DEBUG', 'RELEASE', 'vssver.scc', 'mssccprj.scc']
ignore2 = ['.dsw', '.dsp', '.ncb', '.plg', '.exe']
leftdir = '/a place I worked once had a primitive not-really-source-control way of doing project tracking'
rightdir = '/so I put 2 of the cloned folders here as an expedient'

dcmp = dircmp( leftdir, rightdir, ignore )
#dcmp.report_full_closure()

print_diff_files( dcmp, 'right', ignore2 )
print( '------------------------' )
print_rightonly_files( dcmp, ignore2 )
