

n, m = map(int, input().split())

arr = list(map(int, input().split()))
visited = set()
for i in range(n-1, -1, -1):
    visited.add(arr[i])
    arr[i] = len(visited)

for j in range(m):
    l = int(input())
    print(arr[l-1])
    
    
    

