#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:08:31 2020

Simple implementation of Dijkstra shortest path algorithm

"""
import numpy as np
import sys
import os
import heapq


def ProcessGraph(filename):
    """ 
    Arguments:
        filename -- str, name of the txt file in the directory to be read as a graph
        
    Returns:
        data -- dictionary representation of the graph data as adjacency lists.
                the key represents the starting node. The value is a list of tuples.
                the first element of the tuple is the destinatioon node and the
                second element the distance between the starting node (the key)
                and the destination
    """
    data = {} 
    with open(filename) as file:
        for line in file:
            x=line.split('\t')
            key = int(x[0])
            vals = []
            if x[-1]=='' or x[-1]=='\n':
                x.pop()
            for i in x[1:]:
                 vals.append(tuple(map(int, i.split(','))))
            data.update({key:vals})
    return data
                
            
def Dijkstra(graph, starting_node = 1):
    """
    Returns the shortest distance from starting node to each vertex of graph
    Arguments:
        graph -- dictionary representation of the graph data as adjacency lists.
                the key represents the starting node. The value is a list of tuples.
                the first element of the tuple is the destinatioon node and the
                second element the distance between the starting node (the key)
                and the destination
        starting_node -- int, value of the node from where to compute the shortest distance
    Returns:
        shortest -- dict, keys represent the vertex, value the distance of the 
                    vertex to starting_node
    """
    # number of vertices
    n = len(graph)
    # vertices processed so far
    processed = set()
    processed.add(starting_node)
    # computed shortest path distances
    shortest = {starting_node:0}
    # visit all nodes:
    while len(processed)<n:
        greedy_criterion = np.inf
        for v in processed:
            dist_v = shortest[v]
            for candidates in graph[v]:
                if candidates[0] not in processed:
                    if dist_v + candidates[1]< greedy_criterion:
                        w, greedy_criterion = candidates[0], dist_v+candidates[1]
        shortest.update({w: greedy_criterion})
        processed.add(w)            
    return shortest

def DijkstraHeap(graph, starting_node = 1):
    """
    Returns the shortest distance from starting node to each vertex of graph
    The implementation uses a heap structure
    Arguments:
        graph -- dictionary representation of the graph data as adjacency lists.
                the key represents the starting node. The value is a list of tuples.
                the first element of the tuple is the destinatioon node and the
                second element the distance between the starting node (the key)
                and the destination
        starting_node -- int, value of the node from where to compute the shortest distance
    Returns:
        shortest -- dict, keys represent the vertex, value the distance of the 
                    vertex to starting_node
    """
    # number of vertices
    n = len(graph)
    # vertices processed so far
    processed = set()
    processed.add(starting_node)
    # computed shortest path distances
    shortest = {starting_node:0}
    # visit all nodes:
    #heap=  
    while len(processed)<n:
        greedy_criterion = np.inf
        for v in processed:
            dist_v = shortest[v]
            for candidates in graph[v]:
                if candidates[0] not in processed:
                    if dist_v + candidates[1]< greedy_criterion:
                        w, greedy_criterion = candidates[0], dist_v+candidates[1]
        shortest.update({w: greedy_criterion})
        processed.add(w)            
    return shortest



def PrintResults(shortest, keys):
    """Prints the shortest distances to each element in keys"""
    show = []
    for key in keys:
        show.append(shortest[key])
    print(show)
    return

def main():
    filename = sys.argv[1]
    # keys to look the shortest path of, starting from node 1
    keys = [7,37,59,82,99,115,133,165,188,197]
    # load the graph
    graph = ProcessGraph(filename)
    # compute shortest paths
    shortest = Dijkstra(graph)
    # print shortest paths of keys
    PrintResults(shortest, keys)       

    
    
    
if __name__ == "__main__":
     main()
    

#directory = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/2_graph_search_shortest_path_and_data_structures/week2'
#os.chdir(directory)
#
## keys to look the shortest path of, starting from node 1
#keys = [7,37,59,82,99,115,133,165,188,197]
#
#
#graph = ProcessGraph('dijkstraData.txt')
#shortest = Dijkstra(graph)
#PrintResults(shortest, keys)       
#
#

# run in cmd line: python dijkstra.py dijkstraData.txt
#resutls: [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]

