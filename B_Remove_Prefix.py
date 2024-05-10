
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    seen = set()

    
    for val in arr[::-1]:
        if val in seen:
            break
        else:
            seen.add(val)


    print(len(arr) -  len(seen))
            
