t = int(input())

while t:

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = a + b

    if len(a) >= len(b):
        c.sort()
        print(sum(c[len(b) - 1:]))
    else:
        b.sort(reverse=True)
        print(sum(b[:len(a)]))
    
    t -= 1

