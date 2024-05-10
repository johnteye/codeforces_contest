t = int(input())
for _ in range(t):
    n,s = map(int, input().split())
    arr = list(map(int, input().split()))
   
    left, right = 0, 0 
    res = 0
    ans = []
    sub_sum = 0
    total = sum(arr)
    if total < s:
        print(-1)

    elif total == s:
        print(0)
    else:
        while right < n:
            if sub_sum == s:
                ans.append([right, left])
                res = max(res, right - left + 1)
                sub_sum -= arr[left]
                left += 1
                
            elif sub_sum < s:
                sub_sum += arr[right]
                right += 1
            else:
                
                sub_sum -= arr[left]
                left += 1
     
             
        print(ans)

        




