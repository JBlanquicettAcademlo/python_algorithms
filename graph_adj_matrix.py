
class Graph(object):

    def __init__(self, size):
        self.adj_matrix = []
        self.size = size

        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])

    def add_edges(self, vertex_1, vertex_2):
        if vertex_1 == vertex_2:
            print("same")
        self.adj_matrix[vertex_1][vertex_2]=1

    def remove_edge(self, vertex_1, vertex_2):

        if self.adj_matrix[vertex_1][vertex_2]==0:
            print('No edge')
            return
        self.adj_matrix[vertex_1][vertex_2]=0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print('{:3}'.format(val), end='')

            print()

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

g.print_matrix()