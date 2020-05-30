import sys
import os, time, datetime
from os.path import join, getsize
from datetime import date

reqd_args = 4   # [path] [# o' days] [filter] (+ py script name)

def walk_dir_tree(starting_folder):
    for root, dirs, files in os.walk(starting_folder):
        print root, "consumes",
        print sum(getsize(join(root, name)) for name in files),
        print "bytes in", len(files), "non-directory files"
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
            
def list_recently_modified_files(starting_folder, since, filter):
    
    for root, dirs, files in os.walk(starting_folder):
    
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
            
        for name in files:
            test = name.find(filter)
            if -1 <> test:
                file = join(root, name)
                t = os.path.getmtime(file)
                # 9th item in returned tuple is st_mtime, last modified time
                if datetime.date.fromtimestamp(t) > since:
                    print file
            
if len(sys.argv) < reqd_args :
    print('lists paths/names of recently modified files')
    print('please provide starting path, # of days, filter; e.g.\n"python recentmods.py c:/users/ 1 .txt"')
    exit()

today = date.today()
since_when = today - datetime.timedelta(days=int(sys.argv[2]))

list_recently_modified_files(sys.argv[1], since_when, sys.argv[3])