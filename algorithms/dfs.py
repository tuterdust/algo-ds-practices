class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    def num_nodes(self):
        return len(self.graph.keys())

def dfs_recursively(graph, visited, u):
    visited[u] = True
    print(u, end = " ")
    vertexs = graph.graph[u]
    for node in vertexs:
        if not visited[node]:
            dfs_recursively(graph, visited, node)

def dfs(graph, s):
    visited = [False] * graph.num_nodes()

    dfs_recursively(graph, visited, s)



graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 3)
graph.add_edge(4, 0)
graph.add_edge(4, 5)
graph.add_edge(5, 2)

dfs(graph, 2)
