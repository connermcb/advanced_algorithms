# python3

from sys import stdin

class DGraph():
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.start = -1
        self.end = -1
        self.dist = 0
        self.queue = []
        self.adj_list = [set([]) for i in range(n)]
        self.visited = [False for i in range(n)]
        self.type = [None for i in range(n)]

    
    def read_data(self):
        for i in range(self.m):
            line = [int(x) for x in stdin.readline().split()]
            self.add_edge(line)
        
    def add_edge(self, e):
        v, u = e
        self.adj_list[v-1].add(u)
        self.adj_list[u-1].add(v)
    
    
    def bfs_dist(self):
        while self.queue:
            current = self.queue.pop(0)
            neighbors = [n for n in self.adj_list[current-1]]
            for each in neighbors:
                if self.type[each-1] == self.type[current-1]:
                    return -1
                if self.visited[each-1] == False:
                    self.queue.append(each)
                    self.type[each-1] = (self.type[current-1] * -1)
                    self.visited[each-1] = True
        return 1
                
        
    def is_bipartite(self):
        first = 1
        self.visited[first-1] = True
        self.type[first-1] = 1
        self.queue.append(first)
        result = self.bfs_dist()
        if result == -1:
            return 0
        return result

#l = [(1, 2), (4, 1), (2, 3), (3, 1)]
##l = [(5, 2), (1, 3), (3, 4), (1, 4)]
##l = [(5, 2), (4, 2), (3, 4), (1, 4)]
#
#graph = DGraph(4, 4)
#for each in l:
#    graph.add_edge(each)
#print(graph.is_bipartite())


n, m = (int(x) for x in stdin.readline().split())
graph = DGraph(n, m)
for i in range(m):
    line = [int(x) for x in stdin.readline().split()]
    graph.add_edge(line)

print(graph.is_bipartite())
