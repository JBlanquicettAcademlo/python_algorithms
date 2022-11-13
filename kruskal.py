class Graph:

    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []

    def add_edges(self, u, v, w):
        self.graph.append([u, v, w])


    def find(self, parent, i):
        
        if parent[i]==i:
            return i
        
        return self.find(parent, parent[i])

    
    def apply_union(self, parent, rank, x, y):
        
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if (rank[xroot] < rank[yroot]):
            parent[xroot] = yroot
        
        elif (rank[xroot] > rank[yroot]):
            parent[yroot] = xroot
        
        else:
            parent[yroot] = xroot
            rank[xroot] +=1
    
    def kruskal(self):

        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i +=1
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e+=1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


g = Graph(6)
g.add_edges(0, 2, 4)
g.add_edges(0, 4, 4)

g.add_edges(1, 2, 3)
g.add_edges(1, 3, 3)

g.add_edges(2, 0, 4)
g.add_edges(2, 1, 3)
g.add_edges(2, 3, 4)
g.add_edges(2, 5, 2)
g.add_edges(2, 4, 2)

g.add_edges(3, 1, 3)
g.add_edges(3, 2, 4)
g.add_edges(3, 5, 3)

g.add_edges(4, 0, 4)
g.add_edges(4, 2, 2)

g.add_edges(5, 3, 3)
g.add_edges(5, 2, 2)

g.kruskal()
