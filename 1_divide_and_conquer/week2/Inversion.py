#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:55:24 2020

@author: pablo
"""
import numpy as np
import os

#directory=r'/home/pablo/Documents/learning/algorithms_specialisation/1_divide_and_conquer/week2'
#os.chdir(directory)

#array = np.loadtxt('IntegerArray.txt', delimiter = "\n")

def InversionCount(array):
    
    n= int(len(array))
    #print(array)
    #print(n)
    
    if n ==1:
        return array, 0
    n_half = int(n/2)
    A, inv_A = InversionCount(array[:n_half])
    B, inv_B = InversionCount(array[n_half:])
    
    array_sorted, inv_merge = Merge(A, B)
    
    return array_sorted, inv_A + inv_B + inv_merge
   
    
def Merge(A,B):
    '''
    Takes two lists/arrays of numbers, each sorted in ascending order
    Returns the sorted array resulting from merging A and B, as well as the 
    number of inversions counted in the mere process
    '''
    n_a = len(A)
    n_b = len(B)
    n_c = n_a + n_b
    # Initialise inversions to zeros
    inversions = 0
    # Initialise C
    C = [0]*n_c
    # Initialise indices of A and B
    i = 0
    j = 0
    for k in range(n_c):
        if j>=n_b:
            C[k:] = A[i:]
            return C, inversions
        elif i>=n_a:
            C[k:]=B[j:]
            return C, inversions
            
        elif A[i]>B[j]:
            C[k]=B[j]
            j+=1
            inversions += n_a - i
            #print(' j is :'+str(j))
        else:
            C[k]=A[i]
            i+=1
            #print(' i is :'+str(i))
    return C, inversions
            
#q, w = InversionCount(array)

def main():
    array = np.loadtxt('IntegerArray.txt', delimiter = "\n")
    q, w = InversionCount(array)
    print('The number of inversions is: ' + str(w))

if __name__ == '__main__':
    main()
    