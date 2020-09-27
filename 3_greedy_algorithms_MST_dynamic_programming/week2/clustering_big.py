#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:16:25 2020

@author: pantonar
"""

import numpy as np
from networkx.utils.union_find import UnionFind



def load_data(filename):
    '''
    read the graph in filename path to txt
    return: a 1D array with each     
    '''
    file = open(filename)
    data = []
    count = 0 
    values = {}
    for line in file.readlines(): # ofr non-test cases use file.readlines()- for thest cases use file.readlines()[1:]
        val = int(''.join(line.split()), 2)
        data.append(val)
        if val in values:
            values[val].append(count)
        else:
            values.update({val:[count]})
        count+=1
    return np.array(data), values


    
def number_clusters(cluster):
    ''' returns the number of sets in a UnionFind instance'''
    return len(sorted(map(sorted,cluster.to_sets()))) 

def hamming(num):
    ''' returns a list of all masks for 0, 1 and 2 Hamming distance of num'''
    nbits =num.bit_length()
    mask_1 = [1 << i for i in range(nbits)]
    mask_2 = [ (1 << i )^(1 << j ) for i in range(nbits) for j in range(i+1,nbits)]
    return [0]+mask_1+mask_2
    




def clusterise(values): 
    '''
    Cluster the nodes by hamming distnace lower than 3. Returns the number of resulting clusters
    '''        
    cluster = UnionFind(list(values.keys()))
    for key in values:
        for mask in hamming(key):
            xor = key^mask
            if xor in values:
                cluster.union(xor,key)
    return number_clusters(cluster)


# define graph location
#filename = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/3_greedy_algorithms_MST_dynamic_programming/week2/clustering_big.txt'
# load data
#data, values = load_data(filename)
# return cluster 
def main():
    
    print('Solution should be: 6118')     
    data, values = load_data('clustering_big.txt')
    print(f'The max number of clusters with spacing at least 3 is {clusterise(values)}')
    
    
if __name__ == '__main__':
    main()
    
    
    