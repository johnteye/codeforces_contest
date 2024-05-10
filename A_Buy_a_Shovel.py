# val = '10.3'
# print(val.split('.'))
# print(30%2)

def min_shovels():
    k, r = map(int, input().split())

    i = 1
    while i:
        check = k * i
        if check % 10 == 0:
            return i
        if str(check/10).split('.')[-1] == str(r):
            return i
        
        i += 1
        
print(min_shovels())
