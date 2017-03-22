#python3

from sys import stdin


class Graph():
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.nm = n + m
        self.has_flow = {x:{y:False for y in range(n+1, n+m+1)} for x in range(1, n+1)}
        self.edges = {x:{y:0 for y in range(1, self.nm+2)} for x in range(self.nm+2)}
        for i in range(n):
            self.edges[0][i+1] = 1
        for j in range(n+1, n+m+1):
            self.edges[j][n+m+1] = 1
            
    def add_edge(self, i, data):
        for j in range(len(data)):
            self.edges[i][j+self.n+1] = data[j]
            
    def short_path(self):
        dist = {x:[float('inf'), None] for x in range(0, self.nm+2)}
        dist[0] = [0, None]
        stack = list(range(0, self.nm+2))
        while stack:
            crnt = min(stack, key=lambda x:dist[x][0])
            stack.remove(crnt)
            t = [x for x in self.edges[crnt] if self.edges[crnt][x] != 0]
            for neighbor in t:
                new = dist[crnt][0] + 1
                if new < dist[neighbor][0]:
                    dist[neighbor] = [new, crnt]
        r = self.nm+1
        path = [r]
        if dist[r][1] == None:
            return None
        while r != 0:
            r = dist[r][1]
            path.append(r)
        path = path[::-1]  
        return path
        
    def update_graph(self):
        path = self.short_path()
        if path == None:
            return False
        i, j = path[1:3]
        for i in range(len(path)-1):
            self.edges[path[i]][path[i+1]] = 0
            self.edges[path[i+1]][path[i]] = 1
            if i > 0  and path[i+1] < self.nm+1:
                u, v = sorted(path[i:i+2])
                self.has_flow[u][v] = not self.has_flow[u][v]
        return True
        
     
    def results(self):
        result = [-1 for i in range(self.n)]
        for x in self.has_flow:
            t = [y for y in self.has_flow[x] if self.has_flow[x][y] == True]
            if t:
                result[x-1] = t[0] - self.n
        return result
        
    def get_assignments(self):
        while True:
            sp = self.update_graph()
            if sp == False:
                return self.results()
        return self.results()
        
            
#g = Graph(3, 4)
##l = [(1, 1), (1, 0)]
#l = [(1,1,0,1), (0,1,0,0), (0,0,0,0)]
#for i in range(len(l)):
#    g.add_edge(i+1,l[i])
#
#print(g.get_assignments())

n, m = (int(x) for x in stdin.readline().split())
g = Graph(n, m)
for i in range(n):
    data = [int(x) for x in stdin.readline().split()]
    g.add_edge(i+1, data)
result = " ".join(str(x) for x in g.get_assignments())
print(result)