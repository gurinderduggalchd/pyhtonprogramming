# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:24:02 2018

@author: duggal
"""

from student import student

def main():
    
    surname = input("enter surname of student : ")
    firstname = input("enter first name of student : ")
    stunum = input("enter student number : ")
    course = input("enter course of student : ")
    
    s = student(surname,firstname,stunum, course)
    
    print(s)
    
    print("change surname : ")
    surname = input("enter new surname : ")
    
    s.setsurname(surname)

    print(" change course : ")
    course = input("Enter new course name : ")
    s.setcourse(course)

    print(s)
    
main()

    
    