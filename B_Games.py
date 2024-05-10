from collections import defaultdict
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split())

graph = defaultdict(list)
# print(matrix)
for row in range(len(matrix)):
    for row1 in range(len(matrix)):
        # print(matrix[row1][1])
        if row != row1 :
            # print(row, row1)
            graph[matrix[row][0]].append(matrix[row1][1])


count = 0
for val in graph:
    for num in graph[val]:
        if num == val:
            count += 1


print(count)