#!/usr/bin/env python
import sys
import os

# Takes in one agrment for path of file .pts
file = sys.argv[1]


# counts number of lines in the pts file
num_lines = sum(1 for line in open(file))

# generates header

header = "# .PCD v.7 - Point Cloud Data file format\nVERSION .7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH " + str(num_lines) +"\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS " + str(num_lines) +"\nDATA ascii\n"


def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile+str('.pcd'))

insert(file,header)
