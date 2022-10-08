# Link: https://codeforces.com/problemset/problem/1689/A
#Q: Lex String

t = int(input())

for _ in range(t):
    n, m , k = map(int, input().split())
    a = list(input())
    b = list(input())
    a.sort()
    b.sort()
    
    c = []

    i, j = 0, 0
    A, B = 0, 0

    while i < len(a) and j < len(b):

        if (a[i] < b[j] and A < k) or B >= k:
            c.append(a[i])
            i += 1
            A += 1
            B = 0
        else:
            c.append(b[j])
            j += 1
            A = 0
            B += 1
    
    print("".join(c))
        

