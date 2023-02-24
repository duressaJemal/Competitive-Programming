def solve():
    n, m = map(int, input().split())
    s = input()
    t = input()

    s = s + t[::-1]

    is_valid = True

    index = 0
    while index < n + m:
        curr = s[index]
        j = index

        while j < n + m and s[j] == curr:
            j += 1
        
        if j - index > 2:
            is_valid = False
            break
        
        index += 1
    
    if is_valid:
        print("YES")
        return
    else:
        print("NO")
        return
        

t = int(input())
while t:
    solve()
    t -= 1