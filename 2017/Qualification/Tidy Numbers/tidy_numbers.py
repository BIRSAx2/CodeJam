# Copyright (c) 2018 BIRSAx2. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem B. Tidy Numbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
#'

from argparse import ArgumentParser
import os

def prevtidynumber(N):
    #main algorithm
    for i in range(N,0,-1):
        if str(i)==''.join(sorted(list(str(i)))):
            return i

def row_data(input_data):
    
    for T in input_data[1:]:
        N=T[0]
        prev_n=prevtidynumber(N)
        print('Case #%d: %s' %(input_data.index(T),prev_n))

def read_input(file_name):
    #reading and formatting input data
    file=open(file_name)
    s=[]
    for line in file:
        s.append([int(i) for i in line.rstrip('\n').split(" ")])
    return s
    
def is_valid_file(parser, arg):
    #checks if the file exists
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')
    
def main():
    #reading the command line arguments                           
    parser = ArgumentParser(description="Solution to Google Code Jam 2017 Qualification Round - Problem B. Tidy Numbers", 
    usage=' tidy_numbers.py -i filename')
    parser.add_argument("-i", dest="file_name", required=True,help="Input file name(with extension)", metavar="filename",
    type=lambda x: is_valid_file(parser, x))
    args=parser.parse_args()                            
    input_data=read_input(args.file_name.name)
    row_data(input_data)
                    
if __name__ == '__main__':
    main()
