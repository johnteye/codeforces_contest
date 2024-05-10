def alice_first():
    if max(alice) > max(bob):
        return "Alice"
    elif max(alice) < max(bob):
        return "Bob"
    else:
        return "Alice"
    

def bob_first():
    if max(bob) > max(alice):
        return "Bob"
    elif max(bob) < max(alice):
        return "Alice"
    else:
        return "Bob"
    
t = int(input())
for _ in range(t):
    a_n = int(input())
    alice = list(map(int, input().split()))

    b_n = int(input())
    bob = list(map(int, input().split()))

    print(alice_first())
    print(bob_first())
    