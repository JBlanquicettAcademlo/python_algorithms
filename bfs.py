graph = {
    'v':['c', 'b', 'a'],
    'a':['v', 'b', 'd', 'f'],
    'b':['v', 'a', 'c', 'd', 'e', 'g'],
    'c':['v', 'd', 'g'],
    'd':['a', 'b', 'e'],
    'e':['b', 'd', 'f', 'g', 'k'],
    'f':['a', 'e', 'k'],
    'g':['b', 'c', 'e', 'h'],
    'h':['g', 'k'],
    'k':['e', 'f', 'h']
}

visited = []
queue = []

def bfs(visited, graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'v')