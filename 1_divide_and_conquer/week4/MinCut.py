#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:14:40 2020

@author: pablo
"""
import numpy as np
import os

def FormatAdjacency(adjacency, split = '\t'):
    ''' 
    Takes the adjacecny list as unique argument. Each element ofthe list 
    is a string of elements separated by '\t'. The first such element is the
    code of the vertex. The remaining are the vertices to which the vertex is 
    adjacent to
    '''
    adjacency_dict ={}
    for i in adjacency:
        edges = i.split(split)
        key = edges.pop(0)
        if edges[-1]=='':
            edges.pop(-1)
        adjacency_dict.update({int(key):[int(i) for i in edges]})
    return adjacency_dict

        
def ChooseEdge(adjacency_dict, vertices):
    '''
    Arguments:
        adjacency_dict -- dictionary representing the graph
        vertices -- list of vertices from where to choose an edge
    Returns:
        two vertices defiining an edge
    '''
    picked_vertex_1 = np.random.choice(vertices)
    picked_vertex_2 = np.random.choice(adjacency_dict[picked_vertex_1])
    return picked_vertex_1, picked_vertex_2


def ContractMerge(adjacency_dict, contraction, picked_vertex_1, picked_vertex_2):
    '''
    remove any self loop and references to picked_vertex_1 (as will be merged with picked_vertex2)

    '''
    contraction=list(filter(lambda a: a != picked_vertex_1, contraction))
    contraction=list(filter(lambda a: a != picked_vertex_2, contraction))
    for i in adjacency_dict[picked_vertex_1]:
        ls = [picked_vertex_2 if x==picked_vertex_1 else x for x in adjacency_dict[i]]
        adjacency_dict.update({i:ls})
        if picked_vertex_1 in adjacency_dict[i]: 
            break
    return adjacency_dict, contraction

def RandomizedContraction(adjacency_dict):
    '''
    Argument:
        adjacency_dict -- dictionary representing the graph
    Returns:
        adjacency_dict -- updated graph, resutling from random contractions
        vertices -- list with the 2 remaining vertices after all contractions
        count -- number of cuts resulting from the contraction
    '''
    vertices = list(adjacency_dict.keys())
    while len(vertices)>2:
        # pick a remaining edge, selecteing 2 connected vertices at random
        picked_vertex_1, picked_vertex_2 = ChooseEdge(adjacency_dict, vertices)
        # contract the selected vertices into 1
        contraction = adjacency_dict[picked_vertex_1]+adjacency_dict[picked_vertex_2]
        # remove any self loop and references to picked_vertex_1 (as will be merged with picked_vertex2)
        adjacency_dict, contraction =ContractMerge(adjacency_dict, contraction, picked_vertex_1, picked_vertex_2)
        # Update the adjacency dictionary
        #del  adjacency_dict[picked_vertex_2]
        adjacency_dict.update({picked_vertex_2:contraction})
        # update list of remaining vertices
        vertices.remove(picked_vertex_1)
        # number 
        count =len(adjacency_dict[vertices[0]])
    return adjacency_dict, vertices, count



def main():
    # Open graph
    with open('kargerMinCut', 'r') as f:
        adjacency = f.read().splitlines()
    
    reps = len(adjacency)**2
    min_count = 100000
    for i in range(reps):
        adjacency_dict = FormatAdjacency(adjacency, ' ')
        _, _, count =  RandomizedContraction(adjacency_dict)
        if count<min_count:
            min_count = count
            print(f'New minimum nb of cuts encountered: {min_count}')
        
    print(f'The lowest number of counts encountered in {reps} runs was: {min_count}')
    print(f'Answer is 17')
    
    
if __name__== '__main__':
    main()
        


