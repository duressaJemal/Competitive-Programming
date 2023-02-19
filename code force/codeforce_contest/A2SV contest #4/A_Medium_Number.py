t = int(input())

while t:

    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[1])

    t -= 1