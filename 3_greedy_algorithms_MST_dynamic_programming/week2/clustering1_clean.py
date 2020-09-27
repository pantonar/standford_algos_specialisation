#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:25:06 2020

@author: pantonar

Run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

"""
import time
import numpy as np
from networkx.utils.union_find import UnionFind


def vertices_complete_graph(sorted_edges):
    return int(round((1+np.sqrt(1+8*len(sorted_edges)))/2,0))



def next_candidate_edge(iter_rnd, cluster, sorted_edges):
    row = sorted_edges[iter_rnd]
    i = row[0]
    j = row[1]
    while cluster[i]==cluster[j]:
        row = sorted_edges[iter_rnd]
        i = row[0]
        j = row[1]
        iter_rnd+=1
    return iter_rnd+1


def kruskal_clustering(sorted_edges, desired_clusters=4):
    ''' sorted_edge represents a connected graph'''
    # compute number of vertices
    n_vertices = vertices_complete_graph(sorted_edges)
    # start instance of UnionFind
    cluster = UnionFind(list(range(1,n_vertices+1)))
    # initialise loop
    iter_rnd =0
    stop=0
    while n_vertices!= desired_clusters:
        row = sorted_edges[iter_rnd]
        i = row[0]
        j = row[1]
        if cluster[i]!=cluster[j]:
            cluster.union(i,j)
            # update the number of clusters
            n_vertices -=1
            #print(f"cycle: {iter_rnd}")
            #print(n_vertices)
        else:
            stop+=1
        #update loop cycle
        iter_rnd+=1
    # idedntify the next edge to add to the cluster (i.e. whose vertices belong to different groups)
    iter_rnd = next_candidate_edge(iter_rnd, cluster, sorted_edges)
    # retrieve the minimum maximum space
    min_max_space =sorted_edges[iter_rnd][2]
    return min_max_space, cluster

#### run the algortithm and print the solution 
print('Solution should be: 106')

filename = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/3_greedy_algorithms_MST_dynamic_programming/week2/clustering1.txt'

data=np.loadtxt(filename).astype(int)
sorted_edges = data[data[:,2].argsort()]

tic=time.time()
min_max_space, cluster = kruskal_clustering(sorted_edges, desired_clusters=4)
toc =time.time()
print(f"The solution found by the algo is: {min_max_space}")
print(f"Found in {round(toc-tic,3)}s")
