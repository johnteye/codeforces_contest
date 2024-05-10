from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}

        for i in range(1, n+1):
            self.root[i] = i
            self.height[i] = 1

    def find(self, x):
        if x == self.root[x]:
            return x

        return self.find(self.root[x])
    

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.height[U] > self.height[U]:
                self.root[V] = U
                self.height[U] += self.height[V]
            else:
                self.root[U] = V
                self.height[V] += self.height[U]


n = int(input())
arr = list(map(int, input().split()))
graph = UnionFind(n)


for i in range(1, n+ 1):

    graph.union(i, arr[i-1])

res = 0
for val in graph.root:
    if val == graph.find(val):
        res += 1

print(res)
