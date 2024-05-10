t = int(input())
import math
for _ in range(t):
    n, k = map(int, input().split())

    # arr = []
    count = 0
    for i in range(1000000000):
        if count == k:
            print(i-1)
            break
        if i% n != 0:
            count += 1


