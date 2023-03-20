def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    for index in range(n):
        if arr[index] == 1:
            arr[index] += 1
        
        if index == 0:
            continue

        if arr[index] % arr[index - 1] == 0:
            arr[index] += 1


    print(*arr)

t = int(input())
while t:
    solve()
    t -= 1