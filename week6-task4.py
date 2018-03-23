# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:40:20 2018

@author: 
"""

richter = float(input("Enter the magnitude on richter scale : "))
if richter >= 8.0 :
    print("Most structure fall")
elif richter >= 7.0:
    print("Many building destroyed")
elif richter >= 6.0:
    print("Many building considerably damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

