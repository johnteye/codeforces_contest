n = int(input())
word = list(map(str, input().strip()))
check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_word =  set()

for w in word:
    if w.lower() not in new_word:
        new_word.add(w.lower())

if sorted(new_word) == check:
    print("YES")
else:
    print("NO")

