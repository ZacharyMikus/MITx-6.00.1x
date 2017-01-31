#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:41:42 2017
Author: Zachary W. Mikus

This program is designed to figure out the minimum fixed payment rate required to pay
off a balance within 12 months

"""
#BELOW ARE INPUTTED VARIABLES
balance = 320000
annualInterestRate = 0.2
#BELOW IS MY CODE

monthlyInterestRate = annualInterestRate/12
fixedPayment = 0.01
originalBalance = balance

while balance > 0:
    balance = originalBalance
    for month in range(12):
        balance = balance - fixedPayment
        balance = balance + (monthlyInterestRate*balance)
    if balance > 0:
        fixedPayment += 0.01
print("Lowest Payment: " + str(fixedPayment))
print(balance)