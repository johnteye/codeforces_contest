

n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = (arr[i], i + 1)

group1 = [i for i in arr if i[0] == 1]
group2 = [i for i in arr if i[0] == 2]
group3 = [i for i in arr if i[0] == 3]

matrix = [group1, group2, group3]

ans = [] 

m = min(len(group1), len(group2), len(group3))
res = []
for col in range(m):
    res = []
    for row in range(3):
        res.append(matrix[row][col][1])

    ans.append(res)


if not ans:
    print(0)
else:
    print(len(ans))
    for i in ans:
        print(*i)
        

        
    
