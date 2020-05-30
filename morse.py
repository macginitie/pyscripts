#/usr/bin/python3

import sys

def usage() :
    info = """
    example usage:
    
    python morse.py -d ... --- ...
    
       prints: s o s
       
    python morse.py -e SOS SOS
       
       prints: ... --- ... ... --- ...
       
    python morse.py sometextfile
    
       prints a Morse encoding of sometextfile contents, if English
       [ To DO: prints a decoding of sometextfile contents, if Morse code ]
    """
    print( info )

def encode( char ) :
    if char == 'a' or char == 'A' :   return '.-'
    elif char == 'b' or char == 'B' : return '-...'
    elif char == 'c' or char == 'C' : return '-.-.'
    elif char == 'd' or char == 'D' : return '-..'
    elif char == 'e' or char == 'E' : return '.'
    elif char == 'f' or char == 'F' : return '..-.'
    elif char == 'g' or char == 'G' : return '--.'
    elif char == 'h' or char == 'H' : return '....'
    elif char == 'i' or char == 'I' : return '..'
    elif char == 'j' or char == 'J' : return '.---'
    elif char == 'k' or char == 'K' : return '-.-'
    elif char == 'l' or char == 'L' : return '.-..'
    elif char == 'm' or char == 'M' : return '--'
    elif char == 'n' or char == 'N' : return '-.'
    elif char == 'o' or char == 'O' : return '---'
    elif char == 'p' or char == 'P' : return '.--.'
    elif char == 'q' or char == 'Q' : return '--.-'
    elif char == 'r' or char == 'R' : return '.-.'
    elif char == 's' or char == 'S' : return '...'
    elif char == 't' or char == 'T' : return '-'
    elif char == 'u' or char == 'U' : return '..-'
    elif char == 'v' or char == 'V' : return '...-'
    elif char == 'w' or char == 'W' : return '.--'
    elif char == 'x' or char == 'X' : return '-..-'
    elif char == 'y' or char == 'Y' : return '-.--'
    elif char == 'z' or char == 'Z' : return '--..'
    
    elif char == '1' : return '.----'
    elif char == '2' : return '..---'
    elif char == '3' : return '...--'
    elif char == '4' : return '....-'
    elif char == '5' : return '.....'
    elif char == '6' : return '-....'
    elif char == '7' : return '--...'
    elif char == '8' : return '---..'
    elif char == '9' : return '----.'
    elif char == '0' : return '-----'
    
    return ' ' # punt
    
def decode( char, cap = False ) :
    if char == '.-' : return 'A' if cap else 'a'
    elif char == '-...' : return 'B' if cap else 'b'
    elif char == '-.-.' : return 'C' if cap else 'c'
    elif char == '-..' : return 'D' if cap else 'd'
    elif char == '.' : return 'E' if cap else 'e'
    elif char == '..-.' : return 'F' if cap else 'f'
    elif char == '--.' : return 'G' if cap else 'g'
    elif char == '....' : return 'H' if cap else 'h'
    elif char == '..' : return 'I' if cap else 'i'
    elif char == '.---' : return 'J' if cap else 'j'
    elif char == '-.-' : return 'K' if cap else 'k'
    elif char == '.-..' : return 'L' if cap else 'l'
    elif char == '--' : return 'M' if cap else 'm'
    elif char == '-.' : return 'N' if cap else 'n'
    elif char == '---' : return 'O' if cap else 'o'
    elif char == '.--.' : return 'P' if cap else 'p'
    elif char == '--.-' : return 'Q' if cap else 'q'
    elif char == '.-.' : return 'R' if cap else 'r'
    elif char == '...' : return 'S' if cap else 's'
    elif char == '-' : return 'T' if cap else 't'
    elif char == '..-' : return 'U' if cap else 'u'
    elif char == '...-' : return 'V' if cap else 'v'
    elif char == '.--' : return 'W' if cap else 'w'
    elif char == '-..-' : return 'X' if cap else 'x'
    elif char == '-.--' : return 'Y' if cap else 'y'
    elif char == '--..' : return 'Z' if cap else 'z'
    
    elif char == '.----' : return '1'
    elif char == '..---' : return '2'
    elif char == '...--' : return '3'
    elif char == '....-' : return '4'
    elif char == '.....' : return '5'
    elif char == '-....' : return '6'
    elif char == '--...' : return '7'
    elif char == '---..' : return '8'
    elif char == '----.' : return '9'
    elif char == '-----' : return '0'
    
def encode_string( charstr ) :
    for s in charstr :
        for ch in s :
            print( encode( ch ), end=' ' )
    print()
        
def decode_string( s ) :
    for ch in s :
        print( decode( ch ), end=' ' )
    print()
        
if __name__ == '__main__' :

    if len( sys.argv ) < 2 :
        usage()
        exit()
        
    if sys.argv[1] == '-e' :
        if len( sys.argv ) < 3 :
            usage()
            exit()
        encode_string( sys.argv[2:] )
            
    elif sys.argv[1] == '-d' :
        if len( sys.argv ) < 3 :
            usage()
            exit()
        decode_string( sys.argv[2:] )
        
    else :
        print( 'reading file:', sys.argv[1] )
        for line in open( sys.argv[1] ).readlines() :
            encode_string( line )
        
        
        