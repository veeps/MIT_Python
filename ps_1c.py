#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:04:17 2019

@author: vivianpeng
"""

annual_salary = float(input("Enter your annual salary: "))


rate_of_return = 0.04
semi_annual_raise = .07
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
down_payment = 250000
months = 36

current_savings = 0.0


epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = (high + low)/2.0
while abs(current_savings - down_payment) > epsilon:
    num_guesses += 1
    monthly_salary = annual_salary/12
    monthly_saved = monthly_salary * (guess/10000)
    for months in range(1, months + 1):
        current_savings *= 1 + monthly_rate_of_return
        current_savings += monthly_saved
        if months % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary/12
            monthly_saved = monthly_salary * (guess/10000)  
    prev_guess = guess               
    if current_savings < down_payment :
        low = guess
    else:
        high = guess
    guess= int(round((high + low) / 2))
    if prev_guess == guess:
        break
    
if prev_guess == guess and guess == 10000:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', guess / 10000)
    print('Steps in bisection search:', num_guesses)

  


