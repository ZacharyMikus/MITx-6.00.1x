#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:15:51 2017
Author: Zachary W. Mikus

"""

#BELOW ARE INPUTTED VARIABLES
balance = 101884
annualInterestRate = 0.2
#15552.52
#BELOW IS MY CODE
from decimal import Decimal

monthlyInterestRate = annualInterestRate/12.0
#turns yearly into monthly
originalBalance = balance
#holds the original balance number for the loop
lowerBound = originalBalance/12.0
#Absolute minimum that can be paid per month in 12 month without interest
upperBound = (originalBalance *(1 + monthlyInterestRate)**12)/12.0
#The maximum amount that would be payed in the end of the year
#total balance + interest on the total balance
fixedPayment = lowerBound + (lowerBound/24)

while balance > 0:
    balance = originalBalance
    for month in range(12):
        balance -= fixedPayment
        balance += monthlyInterestRate*balance
    if balance > 0 and balance < lowerBound:
        fixedPayment += 0.1
    elif balance > 0:
        fixedPayment += 0.01
        
#this is for converting and rounding to a two point decimal      
fixedPayment = Decimal(fixedPayment)
paymentOutput = round(fixedPayment, 2)
print("Lowest Payment: " + str(paymentOutput))

    #if balance > 0 and balance < upperBound:  
    #    fixedPayment += 1