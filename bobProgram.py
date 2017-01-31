# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:25:49 2017

@author: kv0t3

This is a program designed to count the number of occurences of the word "bob" in a given string of 's'
"""
s="bobsdbobobafdbobobo"
bobCount = 0
charCount = 0

stringLength = len(s)


for i in range(stringLength):
    if s[charCount] == "b" and s[charCount+1] == "o" and s[charCount+2] == "b":
        bobCount = bobCount + 1
        charCount = charCount + 1
    else:
        charCount = charCount + 1

print("The number of bob's is: " + str(bobCount))


