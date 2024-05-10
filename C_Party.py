from collections import defaultdict
import sys

sys.setrecursionlimit(10**4)
def dfs(sup, depth):
    if not sup:
        return 0
    max_depth = 0
    for employee in graph[sup]:
        
        depth = dfs(employee, depth+ 1 )

        if depth >  max_depth:
            max_depth = depth

    return max_depth + 1


n = int(input())
graph = defaultdict(list)

managers = []
for i in range(n):
    managers.append(int(input()))

for i in range(1, n+1):
    if managers[i-1] == -1:
        continue
    else:
        graph[managers[i-1]].append(i)
res = 0
for i in range(n):
    if managers[i] == -1:
        res = max(res, dfs(i+1, 0))


print(res)