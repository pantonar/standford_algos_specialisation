#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:16:49 2020

@author: pablo

Implementation of Kosaraju's algorithm
"""
import sys
import numpy as np


def AdjacencyList(node_pairs_list, reverse = False):
    """
    Argument:
        noded_pairs_list -- numpy array of dim (n,2). Column 1 is the origin vertex, 
                            column2 the destination. n is the number of edges in the 
                            directed graph
        reverse -- boolean taking True if the adjency list to return is that of 
                    the reversed graph (inverting all edges)
    Returns:
        a dictionary, adjency list representation of the directed graph. 
        keys are the origin vertex, list associated to each key comprise all the 
        destination vertices reachable from the key"""
    adjacency = {}
    added = set()
    for orig, dest in node_pairs_list:
        if reverse:
            orig, dest = dest, orig
        if orig in added:
            adjacency[orig].append(dest)
        else:
            adjacency.update({orig:[dest]})
            added.add(orig)
    return adjacency


def DFS_Topo(graph):
    '''
    Argument:
        graph --  a dictionary representation of a directed graph. Keys are 
                    the origin vertex, list associated to each key comprise all 
                    the destination vertices reachable from the key 
    Returns:
        order -- list containing all the vertices in the graph in topological
                order, as found by the DFS search. The first 'sink' vertex 
                reached is first on the list.
    '''
    order =[]
    visited, finished = set(), set()
    for vertex in range(1, 875714):
        if vertex not in visited:
            frontier = [vertex]
            while frontier:
                node = frontier.pop()
                
                if node not in visited:
                    frontier.append(node)
                    visited.add(node)
                    try:
                        neighbours = graph[node]
                    except KeyError:
                        pass
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            frontier.append(neighbour)
                else:
                    if node not in finished:
                        finished.add(node)
                        order.append(node)
    return order
            
   

def DFS_SCC(graph, order):
    """
    Arguments:
        graph --  a dictionary representation of a directed graph. Keys are 
                    the origin vertex, list associated to each key comprise all 
                    the destination vertices reachable from the key 
        order -- list containing all the vertices in the graph in a given order.
                The function will start DFS search using this ordering. To implement
                Kosoraju's SCC algorithm, order needs to provide the topological 
                oredring of al sinkn vertices
    Returns:
        scc -- dictionary, vertices being the keys and the value the SCC the 
                vertex belongs to
        sorted -- sorted array with the size of each SCC in decreasing order
    """
    num_scc=0
    scc={}
    visited = set()
    sizes = []
    for vertex in reversed(order):
        if vertex not in visited:
            frontier = [vertex]
            num_scc+=1
            size = 0
            while frontier:
                
                node = frontier.pop()
                scc.update({node:num_scc})
                if node not in visited:
                    size+=1
                    visited.add(node)
                    try:
                        neighbours = graph[node]
                        for neighbour in neighbours:
                            if neighbour not in visited:
                                frontier.append(neighbour)
                    except KeyError:
                        pass
            sizes.append(size)
                    
    return scc, sorted(sizes, reverse=True)


def main():
    file = sys.argv[1]
    data = np.genfromtxt(file, dtype=int)
    graph = AdjacencyList(data)
    graph_reversed = AdjacencyList(data, reverse = True)
    order = DFS_Topo(graph_reversed) 
    _, sizes = DFS_SCC(graph, order)
    results = sizes[0:5]
    np.savetxt('output_largest_scc.csv', results, delimiter=',')
    print(results)


    
    

if __name__ == "__main__":
    main()
    


#import os
#
#directory = '/Users/pablo/Documents/learning/coursera/Algorithms specialisation/2_graph_search_shortest_path_and_data_structures/week1'
#os.chdir(directory)
#
#data = np.genfromtxt('SCC.txt', dtype=int)    
#data.shape
#data[:10,:]
#   
#
#graph = AdjacencyList(data)
#graph_reversed = AdjacencyList(data, reverse = True)
#a=DFS_Topo(graph_reversed)  
#aa, size = DFS_SCC(graph, a)


# run in cmd line: python SCC_directed_graph.py SCC.txt
#resutls: [434821, 968, 459, 313, 211]



