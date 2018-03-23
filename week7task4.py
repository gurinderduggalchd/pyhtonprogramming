# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:44:44 2018

@author: 
"""

shoplist = []
itm = ""
flag = 0
while(flag != 1):
    itm = input("Enter the item in shopping list : ")
    if itm == "":
        flag = 1
        break;
    else:
        shoplist.append(itm)
print(shoplist)

