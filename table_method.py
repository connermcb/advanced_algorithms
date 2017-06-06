#python3
# -*- coding: utf-8 -*-
"""
Simplex Method for Linear Programs
"""

import sys

class TableMethod(object):
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.A = []
    
    def get_tableau(self):
        for line in self.A:
            print(line)
    
    def add_line(self, line):
        self.A.append(line)
    
    def add_slack(self):
        for i in range(self.n):
            self.A[i].extend([0 if j!=i else 1 for j in range(self.n)])
            
    def add_rhs(self, line):
        for i in range(self.n):
            self.A[i].append(line[i])
            
l = [[4, 3, 1], [1, 1, 1], [2, 1, -1]]
t = TableMethod(3,3)
for each in l:
    t.add_line(each)
print(t.A)
t.add_slack()
print(t.A)
t.add_rhs([3, 10, 11])
t.get_tableau()
    
    
        
    
        
    
