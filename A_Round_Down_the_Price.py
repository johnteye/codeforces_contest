t = int(input())

for _ in range(t):
    val = int(input())
    for i in range(11):
        if 10 ** i > val:
            sub = 10 ** (i-1)
            print(val - sub)
            break