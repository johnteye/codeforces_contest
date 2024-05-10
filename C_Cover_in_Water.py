t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(str, input().strip()))

    trick = False

    # if len of . is >=3 set trick to true
    # if len of . is <= 2 count += 2
    count = 0
    res = 0
    ans = []
    for right in range(n):
        if arr[right] == ".":
            count += 1
        else:
            ans.append(count)
            count = 0
            
    if count:
        ans.append(count)
    ans.sort()
    if ans[-1] >= 3:
        print(2)
    else:
        print(sum(ans))
