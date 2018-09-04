#    Copyright (c) 2018 BIRSAx2. All rights reserved.
#
    # Google Code Jam 2017 Qualification Round - Problem C. Bathroom segments
    # https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#
import os
from argparse import ArgumentParser

def bathroom_stalls(N,K):

    #Explanation of the algorithm used:

    # This algorithm works on consecutive segments of empty stalls.
    # The data supplied to us are:
    # N: the number of segments
    # K: people are about to enter the bathroom, or better the number of stalls that will be occupied

    # The algorithm finds consecutive segments after each person has occupied a stall:
    # The data will be included in a list, and updated at each processing
    # 1. The number of empty segments is N        list = [N]
    # 2. One person will occupy 1 stall, so the number of empty stalls will be N-1
    # 3. These empty stalls will be divided into two segments of consecutive empty stalls, 
    #     first_segment and second_segment
    #     If N-1 is even then the two segments will be equal length: 
    #     first_segment = second_segment = (N-1) / 2
    #     else the two segments will be of different lengths, 
    #     second_segment < first_segment 
    #     first_segment = (N + 1) / 2 
    #     second_segment = first_segment-1
    #     These two values ​​will replace N in the list   list = [first_segment, second_segment]
    # 4. The next person will choose the largest segment
    # 5. Return to point 1

    # Numerical example:
    # N = 4
    # K = 2

    # First client

    # segments = [4]
    # The length of the largest segment of empty stalls is 4
    # 4-1 is odd then:
    # X=4-1
    # first_segment = (X + 1) / 2
    # second_segment = first_segment-1
    # segments = [2, 1]

    # Second client:

    # segments = [2,1] (the order of segments does not matter, the largest segment will always be chosen)
    # The length of the largest segment of empty stalls is 2
    # 2-1 is odd then:
    # X=2-1
    # first_segment = (X + 1) / 2
    # second_segment = first_segment-1
    # segments = [1, 0, 1]

    # The output consists of the lastest  couple of first_segment and second_segment found
    # Final result : 1 0

    clients=0
    segments=[N] #empty segments
    last=()
    while clients<K:
        clients+=1
        max_index=segments.index(max(segments))
        segments[segments.index(max(segments))]-=1
        Max=segments[max_index]
        first_segment= Max//2 if Max % 2==0 else (Max+1)//2
        second_segment= first_segment if Max % 2==0 else (first_segment-1)
        segments[max_index]=first_segment
        segments.append(second_segment)
        last=(first_segment,second_segment)
    return last

def row_data(input_data):
    # reads each line data and prints output
    for T in input_data[1:]:
        N=T[0]
        K=T[1]
        I=input_data.index(T)
        sol=bathroom_stalls(N,K) if N!=K else (0,0)
        print('Case #%d: %d %d' %(I,sol[0],sol[1]))

def read_input(file_name):
    # reading and formatting input data
    file=open(file_name)
    s=[]
    for line in file:
        s.append([int(i) for i in line.rstrip('\n').split(" ")])
    return s

def is_valid_file(parser, arg):
    # checks if the file exists
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')

def main():
    # reading the command line arguments
    parser=ArgumentParser(usage='python bathroom_stalls.py -i filename', description='Solution to Google Code Jam 2017 Qualification Round - Problem C. Bathroom Stalls')
    parser.add_argument("-i", dest="file_name", required=True,help="Input file name(with extension)", metavar="filename",
    type=lambda x: is_valid_file(parser, x))
    args=parser.parse_args()                            
    input_data=read_input(args.file_name.name)
    row_data(input_data)

if __name__ == '__main__':
    main()
    
