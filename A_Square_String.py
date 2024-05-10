t = int(input())
for _ in range(t):
    arr = list(map(str, input().strip()))
    n = len(arr)
    mid = n // 2
    if n % 2 == 1:
        print('NO')

    elif arr[:mid] == arr[mid:]:
        print('YES')

    else:
        print('NO')