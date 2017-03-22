# python3

from sys import stdin

class DGraph():
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.sources = []
        self.adj_list_in = [set([]) for i in range(n)]
        self.adj_list_out = [set([]) for i in range(n)]
        self.visited = [False for i in range(n)]
    
    def read_data(self):
        for i in range(self.m):
            line = [int(x) for x in stdin.readline().split()]
            self.add_edge(line)
        
    def add_edge(self, e):
        v, u = e
        self.adj_list_out[v-1].add(u)
        self.adj_list_in[u-1].add(v)
    
    def remove_edge(self, e):
        v, u = e
        self.adj_list_out[v-1].remove(u)
        self.adj_list_in[u-1].remove(v)
          
    def explore(self):
        self.sources = [i for i in range(1, self.n+1) if not self.adj_list_in[i-1]]
        while self.sources:
            for i in range(len(self.sources)):
                current = self.sources.pop(0)
                self.visited[current-1] = True
                temp = list(self.adj_list_out[current-1])
                for w in temp:
                    self.remove_edge((current, w))
            self.sources = [i+1 for i in range(self.n) if not self.adj_list_in[i] 
                            and self.visited[i] == False]
        
    def has_cycle(self):
        self.explore()
        for l in self.adj_list_in:
            if l:
                return 1
        return 0

#l = [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)]
#
#graph = DGraph(5, 7)
#for i in range(graph.m):
#    graph.add_edge(l[i])

n, m = (int(x) for x in stdin.readline().split())
graph = DGraph(n, m)
for i in range(m):
    line = [int(x) for x in stdin.readline().split()]
    graph.add_edge(line)
print(graph.has_cycle())


