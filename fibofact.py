#! /usr/bin/python

def fibo( n ) :
    if (n < 1) :
        print('error: invalid argument to fibo()')
        return 0
    if n < 3 :
        return 1
    return fibo( n - 1 ) + fibo( n - 2 )
    
def facto( n ) :
    if (n < 1) :
        print('error: invalid argument to facto()')
        return 0
    if (n == 1) :
        return 1
    return n * facto( n - 1 )

if __name__ == '__main__' :
    for i in range(1,20) :
        print( 'fibo(', i, '):', fibo(i) )
    print()
    for i in range(1,10) :
        print( 'facto(', i, '):', facto(i) )