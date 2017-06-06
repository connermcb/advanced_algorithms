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
            self.A[i].extend([0 if j!=i else 1 for j in range(self.n+1)])
            
    def add_rhs(self, line):
        for i in range(self.n):
            self.A[i].append(line[i])
            
    def add_objective(self, line):
        line = [-1 * x for x in line]
        line.extend([0 if i != self.n else 1 for i in range(self.n+2)])
        self.A.append(line)
            
    def find_pivot(self):
        col = min([each for each in enumerate(self.A[-1][:-1]) if each[1] < 0], key=lambda x:x[1])[0]
        possible_rows = enumerate([self.A[i][-1]/float(self.A[i][col]) for i in range(self.n)])
        row = min([each for each in possible_rows if each[1] > 0], key=lambda x:x[1])[0]
        print(row, col)


        
l = [[4, 3, 1], [1, 1, 1], [2, 1, -1]]
t = TableMethod(3,3)
for each in l:
    t.add_line(each)
print(t.A)
t.add_slack()
print(t.A)
t.add_rhs([3, 10, 10])
t.add_objective([2, -3, 4])
t.get_tableau()
print(t.find_pivot())
    
        
    
        
    
