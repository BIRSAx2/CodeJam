# Copyright (c) 2018 BIRSAx2. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0
#'

from argparse import ArgumentParser
import os

def flip(S,y,K):

    lists=list(S)                               #it is easier to work with lists than with strings
    for i in range(y,y+K):
        lists[i]= '-' if lists[i]=='+' else '+'
    return ''.join(lists)
    
def pancake_flipper(S,K,I):
    #main algorithm
    times=0
    for y in range(len(S)-K+1):
        if S[y]=='-':        
            S=flip(S,y,K)
            times+=1
    print(('Case #%d: %s' %(I,'IMPOSSIBLE' if '-' in S else times)))

def pancake_data(input_data):
    
    for T in input_data[1:]:
        S=str(T[0])
        K=int(T[1])
        pancake_flipper(S,K,input_data.index(T))
        
def read_input(file_name):
    #reading and formatting input data
    file=open(file_name)
    s=[]
    for line in file:
        s.append([(i) for i in line.rstrip('\n').split(" ")])
    return s
    
def is_valid_file(parser, arg):
    #checks if the file exists
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')
    
def main():
    #reading the command line arguments                           
    parser = ArgumentParser(description="Google Code Jam Problem A. Oversized Pancake Flipper", usage=' OversizedPancakeFlipper.py -i filename')
    parser.add_argument("-i", dest="file_name", required=True,help="Input file name(with extension)", metavar="filename",
    type=lambda x: is_valid_file(parser, x))
    args=parser.parse_args()                            
    input_data=read_input(args.file_name.name)
    pancake_data(input_data)
                    
if __name__ == '__main__':
    main()
