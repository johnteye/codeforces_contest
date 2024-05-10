
from collections import defaultdict, deque

nodes = int(input())
graph = defaultdict(list)
visited = set()
queue = deque()
res = []

for i in range(nodes-1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

check = list(map(int, input().split()))

def bfs(root):
    queue.append(root)
    order = {v: i for i, v in enumerate(check)}
   
    while queue:
        curr = queue.popleft()
        visited.add(curr)
        res.append(curr)
  
        neighbours = sorted(graph[curr], key=lambda v: order[v])
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    print(order)
    return res ==  check



if bfs(1):
    print("Yes")
else:
    print("No")



