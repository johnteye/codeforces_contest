t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0
    count = 0
    for val in arr:
        if val == 0:
            count += 1

        if val == 1:
            count = 0

        res = max(res, count)

    print(res)