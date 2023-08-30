from PIL import Image
import sys
import os

def isNum(str):
    '''string -> bool, int'''
    return True, 0

def isDir(path):
    '''string -> bool'''
    return True

def verifyArgs():
    '''void -> string, int
    returns None, [error code] on errors
    -1 = no arguments
    -2 = not a directory
    -3 = too many arguments'''

    av = sys.argv
    ac = len(av)

    if ac == 1:
        return None, -1
    if ac >= 2 and not isDir(av[1]):
        return None, -2
    if ac == 2:
        return av[1], 0
    num = isNum(av[2])
    if ac == 3 and num[0]:
        return av[1], num[1]
    return None, -3

def main():
    '''void -> int'''

    dir, width = verifyArgs()

    if dir == None:
        return 0 - width
    return 0

exit(main())
