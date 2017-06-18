# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:22:47 2017

@author: Zachary
"""


def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    listA = []
    for i in L:
         if g(f(i)) == True:
              listA.append(i)
    L[:] = listA
    if len(L) == 0:
          return -1
    else:
         return max(L)
    
     
     
     
L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)