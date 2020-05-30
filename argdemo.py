#!/usr/bin/python
#
# use Python 3.0

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file (path &) name")
    parser.add_argument("-a", "--aardvark", action = "store_true", 
                        help = "eat ants")
    parser.add_argument("-b", "--bee", action = "store_true", 
                        help = "buzz")
    parser.add_argument("-c", "--cat", action = "store_true", 
                        help = "purr")                        
    args = parser.parse_args()
    no_option = True
    if args.aardvark:
        no_option = False
        print("mmm, yummy ants!")
    if args.bee:
        no_option = False
        print("makin'honey")
    if args.cat:
        no_option = False
        print("purrrrrrrr")
        
    if no_option:
        print("doin' the default thing")
