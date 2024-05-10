num , target = map(int, input().split())
ans = [target]

def whole(num):
    num = str(num).split(".")
    if num[-1] == "0":
        return True
    return False

def trans(target, num):
    if target < num :
        return False
    
    if target == num:

        return True
    
    
    if whole(target/2):
        target =  target/ 2
        ans.append(int(target))
        return trans(target,num)
    
    elif whole((target-1) / 10):
        
        target =  (target-1) / 10
        ans.append(int(target))
        return trans(target, num)

    return 
    
 
    

if trans(target, num):
    print("YES")
    print(len(ans))
    print(*ans[::-1])
else:
    print("NO")




