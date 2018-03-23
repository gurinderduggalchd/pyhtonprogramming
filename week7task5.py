# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:53:28 2018

@author: 
"""

str1 = input("Enter first sentence : ")
str2 = input("Enter second sentence : ")

bigstr = str1 + str2

word = bigstr.split(" ")
print(word)

word.sort()

print(word)

print(" Number of words in the list : ", len(word))
t = tuple(word)
dic = {}
for wrd in t:
    dic = dict.fromkeys(t,t.count(wrd))
            
print(str(dic))


