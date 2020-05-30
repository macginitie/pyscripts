#!/usr/bin/python

class Token :
    def __init__( self ) :
        self.tok_class = 0
        self.tok_str = ''

class Tokenizer :

    # default to C++
    syntax_chars = ',.;:"[]{}()-+=<>~!#%^&*|\\/?'
    syntax_chars += "'\n\t\r\f"
    token_list = []
    debug = True
       
    def __init__( self, syntax = syntax_chars ) :
        self.syntax_chars = syntax
        if self.debug :
            self.debug_print()
                
    def debug_print( self ) :
        for c in self.syntax_chars :
            print( c, end=" " )
            
    def tokenize( self, filename ) :
        srcfile = open( filename ).readlines()
        current_line = 0
        token = ''
        for line in srcfile:
            prevchar = '\n'
            idx = 0
            for char in line:
                if char in self.syntax_chars :                   
                    if token != '' :
                        self.token_list.append( token )
                        token = char
                else :
                    token += char
        if self.debug :
            print( self.token_list )

if __name__ == '__main__' :
    t = Tokenizer()
    #print( "\n-----------------" )
    #q = Tokenizer( "test" )
    t.tokenize( 'mf2.cpp' )