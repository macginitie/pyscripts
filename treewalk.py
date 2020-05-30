import os, time, datetime
from os.path import join, getsize
from datetime import date

def walk_dir_tree(starting_folder):
	for root, dirs, files in os.walk(starting_folder):
		print( root, "consumes", )
		print( sum(getsize(join(root, name)) for name in files), )
		print( "bytes in", len(files), "non-directory files" )
		if 'CVS' in dirs:
			dirs.remove('CVS')  # don't visit CVS directories
			
def list_recently_modified_files(starting_folder, since):
	for root, dirs, files in os.walk(starting_folder):
		if 'CVS' in dirs:
			dirs.remove('CVS')  # don't visit CVS directories
		for name in files:
			file = join(root, name)
			t = os.path.getmtime(file)
			# 9th item in returned tuple is st_mtime, last modified time
			if datetime.date.fromtimestamp(t) > since:
				print( file )
			
#walk_dir_tree('/SourceCode/', date.today())			

today = date.today()
#if (today.day > 2) :
since_when = today - datetime.timedelta(days=2)
#else :    
    #if 
#    since_when = date(today.year, today.month - 1, today.day - 2)
list_recently_modified_files('/SourceCode/', since_when)