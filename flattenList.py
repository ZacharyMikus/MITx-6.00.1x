# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:55:42 2017

@author: Zachary
"""

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    flattenedList = []
    for i in range(len(aList)):
        listOne = aList[i]
        
        if type(listOne) == list:
            for k in range(len(listOne)):
                
                listTwo = listOne[k]
                if type(listTwo) == list:
                    for j in range(len(listTwo)):
                        
                        listThree = listTwo[j]
                        if type(listThree) == list:
                          
                            for z in range(len(listThree)): 
                                listFour = listThree[z]
                                
                                if type(listFour) == list:
                                    flattenedList.append(listFour)    
                                
                                
                                else: 
                                    flattenedList.append(listFour)
                        else:
                            flattenedList.append(listThree)
                else:
                    flattenedList.append(listTwo)
        else:
            flattenedList.append(listOne)
            
            
            
    return flattenedList


print(flatten(aList))