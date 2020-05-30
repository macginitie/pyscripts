import os

# if folder doesn't exist, create it
# NOTE: if a file named 'foldername' exists, this doesn't work
def ensurefolder( foldername ) :
    try :
        check = os.stat( foldername )
    except :
        os.mkdir( foldername )
        

if __name__ == '__main__' :
    ensurefolder( 'layers' )