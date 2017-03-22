# python3

from sys import stdin


class Graph():
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.S = 1
        self.positive = True
        self.source = None
        self.edges = {x+1:{} for x in range(n)}
        self.prev = [0 for i in range(n)]
        self.dist = [float('inf') for i in range(n)]
        self.in_out = {x+1:[0, 0] for x in range(n)}
        
    def add_edge(self, e):
        u, v, w = e
        if w < 0:
            self.positive = False
#        w = -(math.log2(w))
        self.edges[u][v] = w
        self.in_out[u][0] = 1
        self.in_out[v][1] = 1

    def relax_edges(self, u, v):
        
        if self.dist[v-1] > self.dist[u-1] + self.edges[u][v]:
            self.dist[v-1] = self.dist[u-1] + self.edges[u][v]
            self.prev[v-1] = u
    
    def bf_helper(self):
        for u in self.edges:
            for v in self.edges[u]:
                self.relax_edges(u, v)                           
    
                
    def get_source(self):
        pass
                
    def bellman_ford(self):
        if self.m == 0:
            return 0
        self.dist[self.S-1] = 0
        if self.positive == True:
            return 0
        for i in range(self.n-1):
            self.bf_helper()
        test1 = [x for x in list(self.dist) if x < float('inf')]
        self.bf_helper()
        test2 = [x for x in list(self.dist) if x < float('inf')]
        return sum(test2) != sum(test1)

    def detect_neg_cycle(self):
        neg_cycle = False
        sources = [v+1 for v in range(n) if self.dist[v] == float('inf') and 
                   self.in_out[v+1] == [True, True]]
        while sources:
            self.S = sources[0]
            neg_cycle = self.bellman_ford()
            if neg_cycle == True:
                return 1
            sources = [v+1 for v in range(n) if self.dist[v] == float('inf') and 
                       self.in_out[v+1] == [True, True]]
        return 0
            
        
#n, m = 4, 4
#graph = Graph(n, m)

n, m = (int(x) for x in stdin.readline().split())                

graph = Graph(n, m)
#
for i in range(m):
    graph.add_edge([int(x) for x in stdin.readline().split()])

print(graph.detect_neg_cycle())
    
    
#l =[(1, 2, 1), (6, 7, 1), (8, 9, 1), (9, 10, 1), (3, 4, 1), (7, 8, 1),
#    (4, 5, 1), (5, 6, 1), (2, 3, 1)]
##
#l = [(1, 2, -5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]
#
#l = []
#import time
#a = time.time()
#for each in l:
#    graph.add_edge(each)   
#print(graph.edges)
#print(graph.detect_neg_cycle())
#if graph.bellman_ford() == True:
#    print(1)
#else:
#    print(0)

