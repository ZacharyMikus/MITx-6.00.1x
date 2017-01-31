#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:33:13 2017
Author: Zachary W. Mikus

"""
#For tan and pi functions
import math



def polysum(n, s):
    
    #This formula calculates the area of the polygon
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    
    #This formula calculates the perimeter of the polygon
    perimeter = n*s
    
    #polysumResult (Function is called polysum so had to rename)
    #is the sum of the perimeter^2 and area
    polysumResult = area + (perimeter**2)
    
    #This rounds the result to 4 places and returns the value
    #to the function call
    return round(polysumResult, 4)