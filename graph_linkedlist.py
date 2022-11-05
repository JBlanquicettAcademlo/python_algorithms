class Node:

    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):

        self.V = vertices
        self.graph = [None] * self.V


    def add_edges(self, src, dest):

        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):

        for i in range(self.V):
            print(f"Adjacency list of vertex {i}\n head", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next

            print(" \n")

# g = Graph(4)
# g.add_edges(0,1)
# g.add_edges(0,2)
# g.add_edges(0,3)
# g.add_edges(1,2)

g = Graph(8)
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(1,4)
g.add_edges(1,6)
g.add_edges(1,7)
g.add_edges(2,3)
g.add_edges(2,4)
g.add_edges(3,4)
g.add_edges(3,5)
g.add_edges(4,5)
g.add_edges(4,6)
g.add_edges(6,7)

g.print_graph()
