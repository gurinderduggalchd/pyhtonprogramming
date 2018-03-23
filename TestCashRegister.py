# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:40:43 2018

@author: duggal
"""

from cashregister import CashRegister

def main():
    
    cshreg = CashRegister()
    
    price = float(input("Enter price of the item : "))
    
    cshreg.addItem(price)
    
    total = cshreg.getTotal()
    count = cshreg.getCount()
    
    print("total price :", total)
    print("item count :", count)
    
main()

    