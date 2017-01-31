#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:40:51 2017
Author: Zachary W. Mikus


This program is designed to take a balance, an interest rate, and a minimum
payment, assume the minimum monthly payment is being payed, and show the
remaining balance at the end of 12 months.
"""
#START INPUTTED VARIABLES
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#END INPUTTED VARIABLES
#Code below is mine
#
#
from decimal import Decimal
#
monthlyInterestRate = (annualInterestRate/12)
#
for month in range(12):
    monthlyPayment = (monthlyPaymentRate * float(balance))
    #This calculates the minimum monthly payment
    balance = balance - monthlyPayment
    balance = Decimal(balance + (monthlyInterestRate*balance))
    balanceOutput = round(balance,2)
    #adds monthly interest to the balance before printing
print("Remaining balance: " + str(balanceOutput))
