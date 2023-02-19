t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    arr[-1], arr[0] = arr[0], arr[-1] # swap the largest and smallest
    arr[-1], arr[1] = arr[1], arr[-1] # swap the smallest and second smallest

    if arr[0] == arr[1]:
        print("NO")
    else:
        print("YES")
        print(*arr)

    t -= 1