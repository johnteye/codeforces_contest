n = int(input())
arr = list(map(int, input().split()))
arr = [0]+arr+[0]
left, right = 0, 0
res = 0
while right < n:
    if arr[right+1] >= arr[right]:
        right += 1
    else:
        left = right
        right = right + 1
    res = max(res, right - left )

print(res)