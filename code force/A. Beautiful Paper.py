t = int(input())
for _ in range(t):

    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    s1.sort()
    s2.sort()

    is_valid = False

    if s1[1] == s2[1]:
        if s1[0] + s2[0] == s1[1]:
            is_valid = True
    

    
    print("Yes" if is_valid else "No")
