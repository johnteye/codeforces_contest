t = int(input())

for _ in range(t):
    arr = list(map(str, input().strip()))
    res = ""
    res += str(arr[0])
    for i in range(len(arr)):
        if i %2 == 0:
            continue

        else:
            res += str(arr[i])
    print(res)
    