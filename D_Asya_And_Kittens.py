
# class UnionFind:
#     def __init__(self, n):
#         self.root = {}
    

#         for i in range(1, n+1):
#             self.root[i] = i


#     def find(self, x):
#         if x == self.root[x]:
#             return x

#         return self.find(self.root[x])
    

#     def union(self, u, v):
#         U = self.find(u)
#         V = self.find(v)

#         if U != V:
#             self.root[U] = V
                


# n = int(input())
# graph = UnionFind(n)

# for _ in range(n-1):
#     u, v = map(int, input().split())
#     graph.union(u,v)
# a

class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(1, n+1)}
        self.group = {i: [i] for i in range(1, n+1)}

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if len(self.group[rootU]) < len(self.group[rootV]):
                u, v = v, u
                rootU, rootV = rootV, rootU
            self.root[rootV] = rootU
            self.group[rootU].extend(self.group[rootV])
            self.group[rootV] = []

# Read the number of kittens
n = int(input())
graph = UnionFind(n)

# Perform union operations based on input
for _ in range(n-1):
    u, v = map(int, input().split())
    graph.union(u, v)

# Construct the final arrangement
arrangement = [kitten for group in graph.group.values() for kitten in group if group]
print(" ".join(map(str, arrangement)))