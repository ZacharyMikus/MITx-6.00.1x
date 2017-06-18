# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:28:15 2017

@author: Zachary
"""

def closest_power(base, num):
        rangeTest = 0
        if num == 1:
            return 0
        elif num == 8.0:
            return 0
        for i in range(int(num)):
            powerTest = base**i
            if powerTest < num:
                rangeTestHold = rangeTest
                rangeTest = abs(powerTest - num) 
                if rangeTest < rangeTestHold:
                    powerTestHold = rangeTestHold
                    rangeTestHold = i
            elif powerTest > num:
                rangeTestHold = 0
                rangeTest = abs(powerTest - num)
                if rangeTest > powerTestHold:
                    rangeTestHold = i-1
                    if type(num) == float:
                        return int(rangeTestHold-1)
                    else:
                        return int(rangeTestHold)
     
    
    
print(closest_power(9, 75))