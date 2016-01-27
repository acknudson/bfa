from os import listdir
from os.path import isfile, join
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

mypath = sys.argv[1]

fileList = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print fileList
