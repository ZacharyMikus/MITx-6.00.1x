# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:45:25 2017

@author: Zach
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE  

    def multiple(x):
        
        addition_list = []
        
        list_length = len(L)
        
        sumtotal = 0
        
        for i, item in enumerate(L):
            
            expo = (list_length - 1) - i 
            
            sumtotal += item * (x**expo)
        
        return sumtotal
    
    return multiple
    
print (general_poly([1, 2, 3, 4])(10))