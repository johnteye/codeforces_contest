t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().strip()))

    count_a = 0
    count_b = 0

    left = 0
    if arr[left] == "a":
        count_a += 1
    else:
        count_b += 1

    for right in range(1,n):

        if arr[right] == "a":
            count_a += 1

        else:
            count_b += 1

        if count_a == count_b:
            break

        if count_a > count_b and arr[left] == "a":
            left += 1
            count_a -= 1
        elif count_b > count_a and arr[left] == "b":
            left += 1
            count_b -= 1


    if count_a != count_b:
       
        print(-1, -1)

    else:
        print(left+1, right+1)    