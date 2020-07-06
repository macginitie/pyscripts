import math
import sys


"""
given n, return phi*n
"""
def smaller_phi(n):
    return n * (1 + math.sqrt(5))/2.0


"""
given n, return m such that m*phi=n
"""
def larger_phi(n):
    return n / ((1 + math.sqrt(5))/2.0)
    
    
def usage():
    print("usage:\n\tpython phi.py [s|l] n\n\n")
    print("prints the other side length for a golden rectangle having smaller (s) or larger(l) side length n")


if __name__ == '__main__':

    required = 3
    if len(sys.argv) < required:
        usage()
    elif sys.argv[1] == 's':
        print(smaller_phi(float(sys.argv[2])))
    else:
        print(larger_phi(float(sys.argv[2])))