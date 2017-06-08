#python3
# -*- coding: utf-8 -*-
"""
Simplex Method for Linear Programs
"""
import numpy as np
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
            
    def find_pivot_max(self):
        col = min([each for each in enumerate(self.A[-1][:-1]) if each[1] < 0], key=lambda x:x[1])[0]
        possible_rows = enumerate([self.A[i][-1]/float(self.A[i][col]) \
                                   if self.A[i][col] != 0 else float('inf')\
                                   for i in range(self.n)])
        row = min([each for each in possible_rows if each[1] > 0], key=lambda x:x[1])[0]
        return row, col
    
    def find_pivot_solve(self):
        for row in range(self.n):
            col = np.nonzero(self.A[row])[0][0]
            yield row, col
        
    def lcm(self, x, y):
        x= abs(x)
        y= abs(y)
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
   
    def clear_col_max(self, p_row, p_col):
        pivot = self.A[p_row][p_col] 
        for i in [j for j in range(self.n+1) if j != p_row]:
            to_change = self.A[i][p_col]
            if to_change == 0:
                continue
            lcm = self.lcm(pivot, to_change)
            r1 = [self.A[p_row][j]*(lcm/pivot) for j in range(self.m*2+2)]
            r2 = [self.A[i][j]*(lcm/abs(to_change)) for j in range(self.m*2+2)]
            if np.sign(pivot) == np.sign(to_change):
                self.A[i] = list(np.subtract(r2, r1))
            elif np.sign(pivot) != np.sign(to_change):
                self.A[i] = list(np.add(r1, r2))
    
    def clear_col_solve(self, p_row, p_col):
        pivot = self.A[p_row][p_col] 
        for i in [j for j in range(self.n) if j != p_row]:
            print(i)
            to_change = self.A[i][p_col]
            if to_change == 0:
                continue
            lcm = self.lcm(pivot, to_change)
            r1 = [self.A[p_row][j]*(lcm/pivot) for j in range(self.m+1)]
            r2 = [self.A[i][j]*(lcm/abs(to_change)) for j in range(self.m+1)]
            if np.sign(pivot) == np.sign(to_change):
                self.A[i] = list(np.subtract(r2, r1))
            elif np.sign(pivot) != np.sign(to_change):
                self.A[i] = list(np.add(r1, r2))
    
    def check_for_negs(self):
        test = np.array(self.A[-1])
        return (test<0).any()
    
    def gauss_max(self):
        while self.check_for_negs():
            p_row, p_col = self.find_pivot_max()
            self.clear_col(p_row, p_col)
    
    def gauss_solve(self):
        next_pivot = self.find_pivot_solve()
        for i in range(self.n):
            p_row, p_col = next(next_pivot)
            self.clear_col_solve(p_row, p_col)
            
    
    def get_values(self):
        results = []
        for col in range(self.m):
            col_values = [self.A[i][col] for i in range(self.n)]
            if np.count_nonzero(col_values) == 1:
                row = np.nonzero(col_values)[0][0]
                results.append(self.A[row][-1]/self.A[row][col])
            else:
                results.append(0)
        return results
    
    def get_max(self):
        return self.A[-1][-1]/self.A[-1][-2]
    

    
l = [[3,4], [-8,1]]
t = TableMethod(2,2)
for each in l:
    t.add_line(each)

#t.add_slack()
t.add_rhs([1,2])
#t.add_objective([-1,2])
t.get_tableau()
#t.gauss()
t.gauss_solve()
t.get_tableau()


#print()
#t.get_tableau()
#print()
#print(t.get_max())
#print(t.get_values())
#        
    
        
    
