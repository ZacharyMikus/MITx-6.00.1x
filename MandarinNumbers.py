# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:10:57 2017

@author: Zach
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    # FILL IN YOUR CODE HERE
    
    if int(us_num) <= 10:
        return trans[us_num]
    
    elif 11 <= int(us_num) <= 19:
        numberTwo = us_num[1]
        return  trans['10'] + " " + trans[numberTwo]
        
    else:
        numberOne = us_num[0]
        numberTwo = us_num[1]
        if numberTwo == '0':
            return trans[numberOne] + " " + trans['10']
        else:
            return trans[numberOne] + " " + trans['10'] + " " + trans[numberTwo]
    
print(convert_to_mandarin('17'))