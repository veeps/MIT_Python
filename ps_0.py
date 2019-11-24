#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:09:16 2019

@author: vivianpeng
"""

import numpy
import pylab

print("Enter number x:")
user_input_x = input("")
print("Enter number x:",  user_input_x)


print("Enter number y:")
user_input_y = input("")
print("Enter number y:",  user_input_y)



# X**y = 8
a = float(user_input_x)
b = float(user_input_y)
c= a**b
print("X**y =", c)


# log(x) = 1

print("log(x):" , numpy.log2(a))

