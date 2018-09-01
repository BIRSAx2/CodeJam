# Copyright (c) 2018 BIRSAx2. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p3
#
import os
from argparse import ArgumentParser
################# uncomplete
def read_data(filename):
    data=open(filename)
    content=[]
    for line in data:
        content.append(line.rstrip('\n').split(" "))

def is_valid_file(parser,arg):
    # check if the file exists
    if not os.path.exists(parser):
        parser.error("The file %s does not exist"%(arg))
    else:
        return open(arg,'r')

def main():
    # reading the command line arguments
    parser=ArgumentParser(usage='fashion_show -i filename', description='Solution to Google Code Jam 2017 Qualification Round - Problem D. Fashion Show')
    parser.add_argument('-i',required=True, help='Input file name', dest='file_name',
    metavar='filename', type=lambda x:is_valid_file(parser,x))
    arguments=parser.parse_args()
    read_data(arguments.file_name.name)

if __name__=='__main__':
    main()
