#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:29:41 2020

@author: pablo
"""
import numpy as np

def QuickSort(A, l, r , typ ='first'):
    '''
    Arguments:
        A -- Array of n distinct integers
        l -- left endpoint
        r -- right endpoint 
        typ -- type to select the pivot value
    '''
    if l>= r:
        return 0
    else:
        i = ChoosePivot(A, l, r, typ) # i is the position of the pivot value in the array
        # swap A[l] and A[i] to make pivot first
        Swap(A, l, i)
        j = Partition(A, l, r) # j is the new position of the pivot
        m = r-l
        left = QuickSort(A, l, j-1, typ)
        right = QuickSort(A, j+1, r, typ)
        return m + left+right
         
        
    
    
def Partition(A, l, r):
    '''
    Divides the Array A using index l as pivot. Will find the location of the
    pivot by comparing all elements to A[l], and swaping with its latest location
    The pivot vale ends up in index i-1
    '''
    p = A[l]
    i = l+1
    for j in range(i, r+1):
        if A[j]<p:
            Swap(A, i ,j)
            i+=1
    Swap(A, i-1, l)
    return i-1
            
def Swap(A, i, j):
    '''exchanges i -th entry of A with the j-th'''
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp
    return
    
    
def ChoosePivot(A, l, r, typ = 'first'):
    '''return the value p of the pivot'''
    if typ =='first':
        i=l
    elif typ =='last':
        i=r
    elif typ=='random':
        i=np.random.randint(l,r+1)
    elif typ=='median':

        if (r-l+1)%2==0:
            m = int((r-l+1)/2)-1
        else:
            m = int((r-l+1)/2)
        i = Median(A, l, r, m+l)
    else:
        TypeError('Enter a valid type')
    return i


def Median(A, first, last, m):
    ''' returns the median value between a, b and c'''

    dic ={A[first]: first,
          A[m]: m,
          A[last]: last}
    sorted_values = sorted(list(dic.keys()))
    if len(dic)==2:
        return dic[sorted_values[0]]
    return dic[sorted_values[1]]



        
def main():
    for typ in ['first', 'last', 'median']:
        numbers = np.loadtxt('QuickSort.txt', delimiter = "\n")
        count = QuickSort(numbers, 0, len(numbers)-1, typ)
        print(f'Number of comparisons using {typ} as pivot: {count}')

if __name__== '__main__':
    main()
        



