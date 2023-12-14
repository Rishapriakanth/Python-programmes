#The task is to determine whether the given graph is bipartite or not. A graph is considered bipartite if its nodes can be partitioned into two independent sets, denoted as set A and set B, such that each edge connects a node from set A to a node from set B.number of people a
def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1 and not dfs(i, 0):
            return False

    return True

def get_graph_from_input():
    n = int(input())
    graph = []
    for i in range(n):
        neighbors = list(map(int, input().split()))
        graph.append(neighbors)
    return graph
graph1 = get_graph_from_input()
output1 = is_bipartite(graph1)
print(output1)

