#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:46:06 2020

@author: pantonar
Solution to the following assignment:
    
input: jobs.txt

This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

PROBLEM 1:

For example, the third line of the file is "74 59", indicating that the second 
job has weight 74 and length 59. You should NOT assume that edge weights or lengths
are distinct. Your task in this problem is to run the greedy algorithm that 
schedules jobs in decreasing order of the difference (weight - length). Recall 
from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs 
have equal difference (weight - length), you should schedule the job with higher 
weight first. Beware: if you break ties in a different way, you are likely to 
get the wrong answer. You should report the sum of weighted completion times of 
the resulting schedule --- a positive integer --- in the box below.

PROBLEM 2:
Your task now is to run the greedy algorithm that schedules jobs (optimally) in 
decreasing order of the ratio (weight/length). In this algorithm, it does not 
matter how you break ties. You should report the sum of weighted completion 
times of the resulting schedule --- a positive integer --- in the box below.
"""

import sys

def read_data(filename):
    """ Load filename as an array of tuples containing two integers each"""
    with open(filename) as file:
            data =  [(int(line.split(' ')[0]), int(line.split(' ')[1])) for line in file if ' ' in line]    
    return data
    
    
def scores_difference(data):
    """ Get scores of the jobs as differenece of weight - length"""
    return sorted(data, key=lambda t: ((t[0] - t[1]), t[0]), reverse=True)

def scores_ratio(data):
    """ Get the scores of the jobs as the ratio of """
    return sorted(data, key = lambda t:t[0]/t[1], reverse = True)
    
def weigthed_completion_time(data):
    """ Compute weighted completion times required to untertake the jobs oredredd in data"""
    cumul = 0
    weighted_time = 0
    for i in data:
        cumul +=  i[1]
        weighted_time+=i[0]*cumul
    return weighted_time
    


def main():
    filename = sys.argv[1]
    data = read_data(filename)
    data_dif = scores_difference(data)
    data_ratio = scores_ratio(data)
    time_diff = weigthed_completion_time(data_dif)
    time_ratio = weigthed_completion_time(data_ratio)
    print(f" Weighted time, using differences: {time_diff}")
    print(f" Weighted time, using ratio: {time_ratio}")
        
if __name__ == "__main__":
    main()
    
# filename = 'jobs.txt'
#Solutions:
#    - weight - length: 69119377652
#    - weight/length: 67311454237


