#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:38:56 2020

@author: pablo

Simple implementation of Karatsubaś algorithm for integer multiplication

Created on Sun Mar 29 19:44:09 2020

@author: pablo
"""

def KaratsubaMult(x, y):
    '''
    Arguments:
        x -- integer
        y -- integer
        Both x and y must have the same number of digits, that is also required to be even
   Returns:
       The product of x and y using the Karatsuba algorithm
   ''' 
    x =str(x)
    y =str(y)
    n = len(x)
    n_half = int(n/2)
    #print('x is: ' +x)
    #print('y is: ' +y)
    if n_half ==1:
        #print('Base case')
        return int(x)*int(y)
    else:
        a = str(x)[:n_half]
        b = str(x)[n_half:]
        c = str(y)[:n_half]
        d = str(y)[n_half:]
        #print('a is: ' +a)
        #print('b is: ' +b)
        #print('c is: ' +c)
        #print('d is: ' +d)
        ac = KaratsubaMult(a, c)
        ad = KaratsubaMult(a, d)
        bc = KaratsubaMult(b, c)
        bd = KaratsubaMult(b, d)  
    return 10**n*ac + 10**(n_half)*(ad+bc) + bd



KaratsubaMult(111,11111)
a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
KaratsubaMult(a,b) == a*b


print('The result is: ' +str(KaratsubaMult(a,b) ))