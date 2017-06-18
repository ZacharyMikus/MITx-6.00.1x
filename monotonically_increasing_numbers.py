# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:34:18 2017

@author: Zach
"""

L = [10, 4, 3, 8, 3, 2, 4, 5, 7, 7, 2]

def longest_run(L):
    
    def forward_count(L):
        #This clears the lists each time the function runs
        holding_list = []
        saved_list = []
        
        #This runs the length of the function -1 to avoid key index errors
        holding_list.append(L[0])
        
        for i in range(len(L)-1):
            
            #Checks if the first number is greater than the second, And if it is then it adds it to the holding_list
            if L[i] >= L[i + 1]:
                
                holding_list.append(L[i+1])
                
            #Now if the number isn't as large it will check that the holding list is greater than the saved list. If it is, then it's the largest
            #list found so far and copies itself to saved list and clear holding_list
            else:
                
                
                if len(holding_list) > len(saved_list):
                    
                    saved_list = holding_list.copy()
                    
                    holding_list.clear()
                   
                    holding_list.append(L[i+1])
                  
                #If it has found it is NOT the longest list found so far, It will clear and the loop will continue
                else:
                    
                    holding_list.clear()
                    
                    holding_list.append(L[i+1])
            
            
        if len(holding_list) > len(saved_list):
                    
            saved_list = holding_list.copy()
                    
            holding_list.clear()
        
        
        return saved_list
    
    return forward_count(L)

print(longest_run(L))