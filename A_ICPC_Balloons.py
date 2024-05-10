t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().strip()))

    hashmap = defaultdict(str)

    ballons = 0 

    for ballon in arr:
        if ballon not in hashmap:
            ballons += 2
            hashmap[ballon] = True

        else:
            ballons += 1

    print(ballons)