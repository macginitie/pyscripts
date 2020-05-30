#!/usr/bin/python

import sys

# hard-coded tab setting @ 4 spaces !!!
tabSize = 4

def rest_of_line( line, idx ):
    return line[idx:-1] # trim off the trailing '\n'
    
def process( char, context ):
    if context == 'start':
        context = 'test'
    if char == '\t':
        return ' ' * tabSize, context
    elif char == '/':
        return char, context
    elif char == '\n':
        return '', context
    return char, context

def reformat( fname ):
    cfile = open( fname ).readlines()
    context = 'start'
    current_line = 0
    for line in cfile:
        prevchar = '\n'
        modified_line = ''
        idx = 0
        for char in line:
            if char == '/':
                if prevchar == '/':
                    # ignore comments
                    rest = rest_of_line( line, idx )
                    modified_line += rest
                    break
            elif char == '#':
                # ignore preprocessor directives
                modified_line += rest_of_line( line, idx )
                break
            
            newchar, context = process( char, context )
            modified_line += newchar
            prevchar = char
            idx += 1
            
        print( modified_line )
        current_line += 1
        
    #print( 'context is ' + context )

if __name__ == '__main__':
   
    if len(sys.argv) > 1:
        reformat( sys.argv[1] )
        
        