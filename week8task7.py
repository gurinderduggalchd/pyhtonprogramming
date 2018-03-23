# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:36:22 2018

@author: duggal
"""

def mystery(n) :
    if n <= 0 : 
        return 0
    else:
        return mystery(n // 2) + 1


def main():
    num = mystery(20)
    print(num)
main()
