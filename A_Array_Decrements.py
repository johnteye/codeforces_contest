

t = int(input())


for _ in range(t):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    a = max(arr_a)
    b = max(arr_b)

    diff = abs(a- b)
    for i in range(n):
        arr_a[i] = arr_a[i] - diff
        if arr_a[i] < 0:
            arr_a[i] = 0

    
    if arr_a == arr_b:
        print("YES")
    else:
        print("NO")


# print(reduce([3, 5, 4, 1]))