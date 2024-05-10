import heapq
str1 = str(input().lower())
str2 = str(input().lower())

heap = []
heapq.heappush(heap, str1)
heapq.heappush(heap, str2)

if str1 == heap[0] and heap[0] != heap[1]:
    print(-1)


elif str2 == heap[0] and heap[0] != heap[1]:
    print(1)

else:
    print(0)