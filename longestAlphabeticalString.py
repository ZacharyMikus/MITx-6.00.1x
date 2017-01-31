# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:54:31 2017

@author: Zachary Mikus

This is a program designed to take a string input under the variable 's' and
 figure out which characters are in alphabetical order and print the longest string
"""

s=("hijkabcdzefghzbcdef") 

#Finds the length of the string
stringLength = len(s)

s1 = s[0]
#this is the active string
s2 = ""
#this is the stored string

#stringLength is set to negative 1 to avoid index out of range error when
#characterTwo checks the i+1
for i in range(stringLength-1):
    characterOne = ord(s[i])
    #Checks first character
    characterTwo = ord(s[i+1])
    #Checks second character
    if characterTwo >= characterOne:
        #This determines if the second character is in alphabetical order and
        #if it is it will add it to the string 
        s1 = s1 + chr(characterTwo)
    elif len(s1) > len(s2):
        #If the next character isn't in alphabetical order and the current
        #string 's1' is longer than the stored string 's2' then it will replace 
        #it with the longer string
        s2 = s1
        s1 = chr(characterTwo)
    elif len(s1) <= len(s2):
        #If the new string is less than or equal than the string stored in s2
        #the active string will be overwritten and the process will start again
        s1 = chr(characterTwo)

if len(s1) > len(s2):
    s2 = s1
print("Longest substring in alphabetical order is: " + s2[::-1])
#This prints the gfinal output