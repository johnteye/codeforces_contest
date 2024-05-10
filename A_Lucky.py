t = int(input())

for _ in range(t):
    arr = list(map(int, input().strip()))

    res = sum(arr[:3]) == sum(arr[3:])

    if res:
        print("YES")
    else:
        print("NO")