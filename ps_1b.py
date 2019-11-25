#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:35:17 2019

@author: vivianpeng
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
semi_annual_raise = float(input("Enter your semi annual raise: "))
total_cost =   float(input("Enter the cost of your dream home: "))



portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
monthly_saved = monthly_salary * portion_saved


current_savings = 0.0

months = 0

# Number of months:  183

while current_savings < down_payment:
    # problem states investment income and savings deposits occur at the end
    # of the month, so increment month before mutating current_savings
    months += 1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_saved

if months % 6 == 0:
    annual_salary *= 1 + semi_annual_raise
    monthly_salary = annual_salary/12
    monthly_saved = monthly_salary * portion_saved
    
print ("Number of months:", months )   
