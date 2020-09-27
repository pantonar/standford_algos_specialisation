#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:25:06 2020

@author: pantonar

Run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

"""
import time
import numpy as np
import pandas as pd
from networkx.utils.union_find import UnionFind


def vertices_complete_graph(sorted_edges):
    return int(round((1+np.sqrt(1+8*len(sorted_edges)))/2,0))


class UnionFind:
    
    def __init__(self, x):
        self.parents = np.array(range(1,x+1))
        self.sizes = np.ones(x)
        self.groups = len(np.unique(self.parents))
        
    def find(self, object_n):
        parent = self.parents[object_n-1]
        while object_n!= parent:
            object_n = parent
            parent = self.parents[object_n-1]
        return parent
    
    def get_sizes(self, i):
         return self.sizes[self.find(i)-1]
         
    
    def union(self, i, j):
        if self.find(i)==self.find(j):
            print(f"ERROR: {i} and {j} belong to the same group! Cannot apply UNION")
            return
        else:
            if self.get_sizes(i)>self.get_sizes(j):
                self.parents[j-1]=self.find(i)
                assert(self.find(i)==self.find(j))
                self.sizes[i-1]=self.sizes[i-1]+self.sizes[j-1]
            else :
                self.parents[i-1]=self.find(j)
                assert(self.find(i)==self.find(j))
                self.sizes[j-1]=self.sizes[i-1]+self.sizes[j-1]

            self.groups -=1
                

    
cluster=UnionFind(10)
cluster.groups
cluster.union(1,2)
cluster.groups
cluster.union(5,6)
cluster.union(5,1)
cluster.union(5,4)
cluster.union(9,10)
cluster.union(7,8)

            
        
graph =pd.read

filename = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/3_greedy_algorithms_MST_dynamic_programming/week2/clustering1.txt'
with open(filename) as file:
    raw_data = file.readlines()
    
data=np.loadtxt(filename).astype(int)
sorted_edges = data[data[:,2].argsort()]

data.columns = ['vertex1', 'vertex2', 'similarity']
sorted_edges = data.sort_values(by='similarity', axis=0)


filename = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/stanford-algs/testCases/course3/assignment2Clustering/Question1'
case = '/input_completeRandom_28_512.txt'
data=np.loadtxt(filename, skiprows=1).astype(int)
sorted_edges = data[data[:,2].argsort()]

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
            print(f"cycle: {iter_rnd}")
            print(n_vertices)
        else:
            stop+=1
        #update loop cycle
        iter_rnd+=1
    # idedntify the next edge to add to the cluster (i.e. whose vertices belong to different groups)
    iter_rnd = next_candidate_edge(iter_rnd, cluster,sorted_eddges)
    # retrieve the minimum maximum space
    min_max_space =sorted_edges[iter_rnd][2]
    return min_max_space, cluster
    
head=[]
for row in range(vertices_complete_graph(sorted_edges)):
    head.append(cluster.find(row))
np.unique(head)    

    i = row[0]
    j = row[1]
    if has_cycles(i,j):
        
            
            
filename = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/stanford-algs/testCases/course3/assignment2Clustering/Question1'
case = '/input_completeRandom_16_64.txt'
data=np.loadtxt(filename+case, skiprows=1).astype(int)
sorted_edges = data[data[:,2].argsort()]          
            
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
        print(f"cycle: {iter_rnd}")
        print(n_vertices)
    else:
        stop+=1
    #update loop cycle
    iter_rnd+=1
row = sorted_edges[iter_rnd]
i = row[0]
j = row[1]
while cluster[i]==cluster[j]:
    row = sorted_edges[iter_rnd]
    i = row[0]
    j = row[1]
    iter_rnd+=1
        
min_max_space =sorted_edges[iter_rnd-1][2]
min_max_space
            
            