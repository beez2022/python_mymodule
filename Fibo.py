# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:23:46 2022

@author: beekheng
"""

class Fib:
          
    
    def __iter__(self):
        return self
    
    def __init__(self,max):
        self.upto = max
        self.current = 1
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
    
    def __next__(self):
        if self.current <= self.upto:
           if self.current == 1 or self.current == 2:
               self.n3 = 1
               self.n1 = 1
               self.n2 = 1
               self.current += 1
               return(self.n3)
           else:
               self.n3 = self.n1 + self.n2
               self.current += 1
               self.n1 = self.n2
               self.n2 = self.n3
               return self.n3
        else:
           raise StopIteration