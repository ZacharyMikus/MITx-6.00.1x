#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:52:37 2017

@author: Zachary Mikus
"""
print("Hello welcome to this character conversion program!")
print("Do you wish to convert a number to a character?")
print("Or a character to a number?")
decision = input("Please type "char" for to find a numbers character or "num" to find a characters number.").lower()


if decision == "char":
	rawCharacter = input("Please input the character you wish to convert: ")
	asciiNumber = ord(rawCharacter)
#Converts to a number
	print(asciiNumber)

elif decision == "num":

	charNumber = int(input("Please input the number you wish to convert to a character: "))
	character = chr(charNumber)
#converts integer into text
	print(character)

print("Thank you for using this program")
