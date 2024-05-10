t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even = []
    odd = []
    

    for i in range(n):
        if (i+1) % 2 == 0:
            even.append(arr[i])

        else:
            odd.append(arr[i])

    e_flag =  all(idx % 2 == 0 for idx in even) or all(idx % 2 != 0 for idx in even)
    o_flag =  all(idx % 2 == 0 for idx in odd) or all(idx % 2 != 0 for idx in odd)


    if e_flag and o_flag:
        print("YES")

    else:
        print("NO")

    