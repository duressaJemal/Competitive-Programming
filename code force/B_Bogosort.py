t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))
    print(*sorted(arr, reverse=True))

    t -= 1




