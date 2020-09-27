#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:17:54 2020

Implementation of the median maintenance algorithm
-takes a stream of numbers
-keeps track of the sum of medians
-updadtes the meian value resulting from the new element in the stream
"""
from heapq import *
import os
import numpy as np
import sys
import time

#directory = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/2_graph_search_shortest_path_and_data_structures/week3'
#os.chdir(directory)
# solution: 1213

    
class median_maintenance:
    
    def __init__(self,value):
        self.H_high = [] # supports extract min   
        self.H_low = [] # supports extract max
        heappush(self.H_low, -value)
        self.median = value
        self.median_sum = value
        
    def new_val(self, value):
        """add to heap containing the lower values if value lower than the maximum"""
        if value< -self.H_low[0]:
            heappush(self.H_low, -value)
        else:
            heappush(self.H_high, value)
        self.check_inbalance() # ensure heaps are balanced
        self.update_median() # updates the median attribute
        self.update_sum()
        
    def check_inbalance(self):
        """
        Ensures that H_low and H_high have the same number of elements
        If total elements are odd, H_low will always have one element more
        """
        while len(self.H_low)>=len(self.H_high)+1:
            heappush(self.H_high, -heappop(self.H_low))
        while len(self.H_low)<len(self.H_high):
            heappush(self.H_low, -heappop(self.H_high))
    
    def update_median(self):
        """ Upadte the median attribute"""
        if len(self.H_low)>=len(self.H_high):
            self.median = -self.H_low[0]
        elif len(self.H_low)<len(self.H_high):
            self.median = self.H_high[0]

    def update_sum(self):
        """ Keep track of the sum of medians so far"""
        self.median_sum+=self.median


def ReadNumbers(filename):
    """
    Argument:
        filename -- str, txt file containing a list of numbers, one per line
    Returns:
        data -- list, containing each number in filename as an integer
    """
    with open(filename) as file:
        data = [int(line.strip('\n')) for line in file]
    return data
    
def ReturnRelevantDigits(median_sum, modulo = 10000):
    return median_sum%modulo
    

def main():
    # name of file containing the data
    filename = sys.argv[1]
    tic = time.time()
    # read the data
    values = ReadNumbers(filename)
    # initialise median_maintenance class
    median = median_maintenance(values[0])
    # start the stream
    for i in range(1, len(values)):
        median.new_val(values[i])
    # get the sum modulo 10000 and print it
    median_sum = ReturnRelevantDigits(median.median_sum, 10000)
    toc = time.time()
    print(toc-tic)
    print(f"The sum of medians modulo 10,000 is {median_sum}")
    
if __name__ == "__main__":
    main()

# run in the command line: python MedianMaintenance.py Median.txt
# filename = 'Median.txt'
# filename = 'assignment3Median/input_random_40_5120.txt'
# filename = 'assignment3Median/input_random_44_10000.txt'
## Compare time required dusing the naive implementation:
#tic=time.time()
#med_sum=0
#for i in range(len(values)):
#    med_sum+=np.median(values[:i+1])
#toc = time.time()
#print(toc-tic)
    