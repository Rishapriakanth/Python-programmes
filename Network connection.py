#goal is to find the minimum number of operations required to achieve full connectivity of all cities in the region.
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def min_operations_for_full_connectivity():
    N = int(input())
    M = int(input())

    routes = []
    for _ in range(M):
        route = list(map(int, input().split()))
        routes.append(route)

    uf = UnionFind(N)

    components = N
    for route in routes:
        if uf.find(route[0]) != uf.find(route[1]):
            uf.union(route[0], route[1])
            components -= 1

    result = components - 1 if components > 1 else 0
    return result


output1 = min_operations_for_full_connectivity()
print(output1)
