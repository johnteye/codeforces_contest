arr = list(map(int, input().strip()))

dangerous = False
count = 1
for i in range(1, len(arr)):

    if arr[i-1] == arr[i]:
        count += 1
        if count >=7 :
            dangerous = True
            break
    else:
        count = 1
if dangerous:
    print("YES")
else:
    print("NO")

# def helper(arr):
#     count = 0
#     res = float("-inf")
#     for val in arr:
#         res = max(res, count)
#         if val == 0:
#             count += 1

#         else:
           
#             count = 0

#     return res


# def help(arr):
#     count = 0
#     res = float("-inf")
#     for val in arr:
#         res = max(res, count)
#         if val == 1:
#             count += 1

#         else:
#             count = 0
        
#     return res

# if help(arr) >= 7  or helper(arr) >= 7:
#     print("YES")
# else:
#     print("NO")










# def helper():
        
#     count = []
#     for val in arr:

#         if not count:
#             count.append([val, 1])
#         if count[0][1] >= 7:
#             return print("YES")
        
#         if val == count[0]:
#             count[0][1] += 1
#         else:
#             if count[0][0]  != val:
#                 count[0][0] = val
#                 count[0][1] = 1
#             count[0][1] += 1
#     return print("NO")

# helper()
    
