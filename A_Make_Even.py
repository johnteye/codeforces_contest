# the number gets even in the even number is at the end

t = int(input())
for _ in range(t):
    value = list(map(int, input().strip()))
    
    if value[-1] % 2 == 0:
        print(0)
    elif value[0] % 2 == 0:
        print(1)

    else:
        for val in value:
            if val%2 == 0:
                print(2)
                break
        else:
            print(-1)


        