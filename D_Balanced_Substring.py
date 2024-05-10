
n = int(input())
arr = list(map(int, input().strip()))

count_a = 0
count_b = 0
res = 0

left = 0
if arr[left] == 0:
    count_a += 1
else:
    count_b += 1

for right in range(1,n):

    if arr[right] == 0:
        count_a += 1

    else:
        count_b += 1

    if count_a == count_b:
        res = max(res, (right-left))
        continue
        

    if count_a > count_b and arr[left] == 0:
        left += 1
        count_a -= 1
    elif count_b > count_a and arr[left] == 1:
        left += 1
    
        count_b -= 1





print(res)