def solve():
    n = int(input())
    arr = list(input().lower())
    new = []

    prev = ""

    for char in arr:
        if char != prev:
            new.append(char)
            prev = char
    
    if new == ["m", "e", "o", "w"]:
        print("YES")
    else:
        print("NO")
        
t = int(input())
while t:
    solve()
    t -= 1