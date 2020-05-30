#!/usr/bin/python

folderloc = '/src/dox/wordsEn/' 
filename = folderloc + 'wordsEn.txt'

if __name__ == '__main__' :

    wordlist = open( filename ).readlines()
    # print( wordlist[:10] )
    count = 0
    for word in wordlist :
        count += 1
        #if (word[:-1] == 'tenebrific') :
        if (word[:-1] == 'ordinary') :
            print( 'word #', count )
            exit()
        if (count % 100 == 0) :
            print( '.', end='' )
    print( 'missing' )