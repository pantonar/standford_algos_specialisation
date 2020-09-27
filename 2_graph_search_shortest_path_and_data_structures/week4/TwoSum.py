#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:22:51 2020

@author: pablo
solution: 427
"""

from bisect import *
import time
import os
import sys

#directory = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/2_graph_search_shortest_path_and_data_structures/week4'
#os.chdir(directory)

###############################################################################
### Implementation using the Has table
### Takes about 2h to run (need to perform 20,000 * 1,000,000 operations)
### a better approach is needed
def ReadData(filename):
    """ Load filename as an array of integers"""
    with open(filename) as file:
        data =  [int(line) for line in file]    
    return data

def DataToDict(data):
    """Read the array data as dict keys"""
    return {i:'' for i in data}

def CheckSum(data, data_dict, target):
    """ 
    Check for each element of the array data if there is another value y in the 
    hash table that adds up to the target
    """
    for i in range(len(data)):
        val = data[i]
        y = target - val
        if y != val:
            if y in data_dict:
                return True
    return False

### check for all targets between -10000 and 10000
#tic =time.time()
#for n in range(-10000, 10001):
#    if n%1000==0:
#        print(n)
#    if CheckSum(data, data_dict, n):
#        count+=1
#print(count)
#print(f"time taken: {time.time()-tic} s")  


###############################################################################   
### Implementation using binary search
### reduce the amount of hash checks to sensible values of y for every x in        


class TwoSumsSearch:
    def __init__(self, filename):
        self.ReadData(filename)
        self.data.sort()
        
    def ReadData(self, filename):
        """ Load filename as an array of integers"""
        with open(filename) as file:
            self.data =  [int(line) for line in file]    
        
    def FindSum(self):
        """
         For each entry of self.data, reduce the number of valid y values that
         could yield to the sum falling in [-10000,10000]. Then count these 
         values keeping track of them not being repeated.
         The reduction in the #y is achieved via binary search
        """
        s=set()
        for x in self.data:
            low = -10000-x
            high = 10000-x
            p=bisect_left(self.data, low)
            q=bisect_right(self.data, high)
            
            for y in self.data[p: q]:
                if y!=x:
                    assert(x+y>=-10000 and x+y<=10000)
                    s.add(x+y)
        self.two_sums = len(s)
                
        
        
        


def main():
    filename = sys.argv[1]
    two_sums_search = TwoSumsSearch(filename) 
    two_sums_search.FindSum()
    #two_sums_search.two_sums  
    print(f"The number of target values reached is {two_sums_search.two_sums}")

if __name__=="__main__":
    main()
#
#filename = '2sums.txt'
#filename = 'assignment4TwoSum/input_random_27_640.txt'
#data=ReadData(filename)
#data.sort()
#data_dict = set(data)
#count = 0
#     
#        
#
#
#CheckSum(data, n)
#print(time.time()-tic)
#
#
#filename = 'assignment4TwoSum/input_random_52_40000.txt'
#data=ReadData(filename)
#data.sort()
#data_dict = set(data)
#print(len(data_dict))
#it={}
#s=set()
#for x in data:
#    low = -10000-x
#    high = 10000-x
#    p=bisect_left(data, low)
#    q=bisect_right(data, high)
#    
#    for i in data[p: q]:
#        if i!=x:
#            assert(x+i>=-10000 and x+i<=10000)
#            s.add(x+i)
#
#print(len(s))
#

### Run: python TwoSumn




