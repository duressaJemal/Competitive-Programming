def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    count = 0
    t_outlet = 2

    for val in arr:
        if t_outlet >= n:
            break
        else:
            t_outlet += (val - 1)
            count += 1
    
    if t_outlet >= n:
        print(count)
    else:
        print(-1)
    return

t = int(input())
while t:
    solve()
    t -= 1