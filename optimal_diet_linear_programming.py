#python3
# -*- coding: utf-8 -*-
"""
Optimal Diet Problem - Linear Programs
"""
import decimal
decimal.getcontext().prec = 15
import itertools as it
import numpy as np
import sys


class Matrix():
    
    def __init__(self, n, matrix=None):
        self.n = n
        if matrix:
            self.matrix = matrix
        else:
            self.matrix = []
        self.current_col = 0
        self.current_row = 0
        
    def get_matrix(self):
        for line in self.matrix:
            print(line)
        
    def add_line(self, line):
        self.matrix.append(line)
        
    def swap(self, i): 
        self.matrix[self.current_row], self.matrix[i] = list(self.matrix[i]), list(self.matrix[self.current_row])
        
    def divide(self, i):
        divisor = self.matrix[i][self.current_col]
        self.matrix[i] = [x/divisor for x in self.matrix[i]]

        
    def add_subtract(self):
        for i in [x for x in range(len(self.matrix)) if x != self.current_row]:
            mult = self.matrix[i][self.current_col]/self.matrix[self.current_row][self.current_col]
            temp = [x*mult for x in self.matrix[self.current_row]]
            self.matrix[i] = [x-y for x, y in zip(self.matrix[i], temp)]
        

    def get_leftmost(self):
        if self.current_row == self.n:
            return None
        else:
            for i in range(self.current_row, len(self.matrix)):
                if self.matrix[i][self.current_col] != 0:
                    return i
        self.current_col += 1
        return self.get_leftmost()
                
                
    def gaussian(self):

        while self.current_col < self.n:
            self.swap(self.get_leftmost())
            self.divide(self.get_leftmost())
            self.add_subtract()
            self.current_col += 1
            self.current_row += 1

    
    def solve_matrix(self):
        result = [None for i in range(self.n)]
        for line in self.matrix:
            if sum(line[:-1]) == 1:
                result[line.index(1)] = line[-1]
#        for i in range(self.n):
#            if sum(self.matrix[i][:-1]) != 1:
        return result



class Optimal(object):
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.A = []
        self.subset_idcs = list(it.combinations(range(n+m), r=m))
        self.results = []

        
    def read_coef(self, line):
        self.A.append(line)
        
    def read_right_vector(self, line):
        for each in enumerate(line):
            i, vi = each
            self.A[i].append(vi)
            
    def read_pleasure(self, line):
        self.pleasure_vector = np.array(line)
        
    def add_dish_mins(self):
        """
        Appends to matrix A amount i > 0 for each amount in m.
        """
        for i in range(self.m):
            temp = [decimal.Decimal('0') for j in range(self.m+1)]
            temp[i] = decimal.Decimal('1')
            self.A.append(temp)

    def test_helper(self, v):

        for row in self.A[:self.n]:
            if sum(np.array(row[:-1]) * v) > row[-1]:
                return False
        return True
    
    def test_subsets(self):
        for each in self.subset_idcs:
            matrix = [self.A[i] for i in each]
            m = Matrix(n=self.m, matrix=matrix)
            m.gaussian()
            self.results.append(m.solve_matrix())
        self.results = [np.array(each) for each in self.results if None not in each and \
                        all(map(lambda x:x>=0, each))]
        self.results = [(each, sum(each*self.pleasure_vector)) for each in self.results]
        self.results = [each for each in self.results if self.test_helper(each[0])]
        result = max(self.results, key=lambda x:x[1])[0]
        return [float(x) for x in result]
        



n, m = [int(each) for each in sys.stdin.readline().split()]
O = Optimal(n, m)
for i in range(n):
    line = [decimal.Decimal(each) for each in sys.stdin.readline().split()]
    O.read_coef(line)   
line = [decimal.Decimal(each) for each in sys.stdin.readline().split()]
O.read_right_vector(line)
line = [decimal.Decimal(each) for each in sys.stdin.readline().split()]
O.read_pleasure(line)
O.add_dish_mins()
results=O.test_subsets()
print("Bounded solution")
for each in results:
    print(each, end=" ")


#l = ["3 2", "-1 -1", "1 0", "0 1", "-1 2 2", "-1 2"]
#for i in range(len(l)):
#    if i == 0:
#        n, m = [int(each) for each in l[i].split()]
#        O = Optimal(n, m)
#    elif i>0  and i<n+1:
#        line = [decimal.Decimal(each) for each in l[i].split()]
#        O.read_coef(line)
#    elif i==n+1:
#        line = [decimal.Decimal(each) for each in l[i].split()]
#        O.read_right_vector(line)
#    elif i==n+2:
#        line = [decimal.Decimal(each) for each in l[i].split()]
#        O.read_pleasure(line)

#O.add_dish_mins()
##for line in O.A:
##    print(line)
#print(O.test_subsets())

