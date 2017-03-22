#python3

from sys import stdin

class Matrix():
    
    def __init__(self, n):
        self.n = n
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
        self.matrix[i] = [x/float(divisor) for x in self.matrix[i]]

        
    def add_subtract(self):
        for i in [x for x in range(len(self.matrix)) if x != self.current_row]:
            mult = self.matrix[i][self.current_col]/float(self.matrix[self.current_row][self.current_col])
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
        
        
            


n = int(stdin.readline())
m = Matrix(n)
for i in range(n):
    m.add_line([int(x) for x in stdin.readline().split()])
m.gaussian()
print(' '.join([str(x) for x in m.solve_matrix()]))


