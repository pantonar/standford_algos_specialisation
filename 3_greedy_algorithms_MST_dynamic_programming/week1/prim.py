#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:32:02 2020

@author: pantonar

Implementation of Prims's algorithm for MST computation

input: edges.txt

This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there 
is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that 
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. 
You should report the overall cost of a minimum spanning tree --- an integer, 
which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) 
time implementation of Prim's algorithm should work fine. OPTIONAL: For those 
of you seeking an additional challenge, try implementing a heap-based version. 
The simpler approach, which should already give you a healthy speed-up, is to 
maintain relevant edges in a heap (with keys = edge costs). The superior 
approach stores the unprocessed vertices in the heap, as described in lecture. 
Note this requires a heap that supports deletions, and you'll probably need to 
maintain some kind of mapping between vertices and their positions in the heap.

"""
import sys
import numpy as np

def read_graph(filename):
    """ read graph as a list"""
    with open(filename) as file:
        raw_data = file.readlines()
    return raw_data

def process_raw_data(raw_data):
    """ Return an adjacency list representation of the raw graph. The keys 
    are the nodes, the values a list of tuples corresponding respectively to 
    the nodes connected to the key and the cost to reach them """
    data = {}
    for i in raw_data[1:]:
        i = i.replace('\n', '')
        i = i.split(' ')
        i=[int(x) for x in i]
        if i[0] in data.keys():
            val = data[i[0]]
            val.append((i[1], i[2]))
            data.update({i[0]:val})
        else:
            data.update({i[0]:[(i[1], i[2])]})
            
        if i[1] in data.keys():
            val = data[i[1]]
            val.append((i[0], i[2]))
            data.update({i[1]:val})
        else:
            data.update({i[1]:[(i[0], i[2])]})
    return data
    
def prim_mst(data):
    v = set(data.keys())
    x = set([1])
    tree = set()
    cost = 0
    passes=0
    while x!=v:
        val = np.inf
        #edge = None
        
        for visited in x:
            options = data[visited]
            for option in options:
                if option[0] in v-x:
                    if option[1]<val:
                        vertex = option[0]
                        val = option[1]
                        edge = set([visited, vertex])
                        
                        
        x.add(vertex)
        tree.add(frozenset(edge))
        cost+=val
        passes+=   1
    return tree, cost
        
                    
        
    
filename = 'edges.txt'    
#filename = 'test_cases_assignment1/assignment1SchedulingAndMST/question3/input_random_50_10000.txt'

raw_data = read_graph(filename)
data = process_raw_data(raw_data)
mst, cost = prim_mst(data)
print(cost)
    







