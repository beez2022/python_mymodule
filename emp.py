# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 09:40:43 2022

@author: beekheng
"""

class Employee:
# initialization
    def __init__(self, fname, lname, number):
        self._firstname = fname
        self._lastname = lname
        self._num = number

# property getters

    @property
    def first(self):
        return self._firstname

    @property
    def last(self):
        return self._lastname

    @property
    def number(self):
        return self._num

# property setters
    @first.setter
    def first(self, var):
        self._firstname = var

    @last.setter
    def last(self, var):
        self._lastname = var
    
    @number.setter
    def number(self, var):
        self._num = var

# Instance Method
    def print_name(self):
        print("New Employee is", self._firstname, self._lastname, self._num)