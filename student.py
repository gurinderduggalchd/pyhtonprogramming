# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:06:25 2018

@author: duggal
"""

class student():
    def __init__(self, surname, firstname, stunum, course):
        self.surname = surname
        self.firstname = firstname
        self.stunum = stunum
        self.course = course
    
    def getsurname(self):
        return self.surname
    
    def setsurname(self,surname):
        self.surname = surname
    
    def getfirstname(self):
        return self.firstname
    
    def setfirstname(self,firstname):
        self.firstname = firstname
    
    def getstudentnumber(self):
        return self.stunum
    
    def setstudentnumber(self, stunum):
        self.stunum = stunum
    
    def getcourse(self):
        return self.course
    
    def setcourse(self,course):
        self.course = course
        
    def __str__(self):
        return "Surname : %s \t First Name :%s \t  Student number : %s \t Course : %s " % (self.surname, self.firstname, self.stunum, self.course)


    
    