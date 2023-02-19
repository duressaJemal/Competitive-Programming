t = int(input())

while t:

    n, c = map(int, input().split())
    arr = list(map(int, input().split()))

    for index in range(n):
        arr[index] += (index + 1)
    arr.sort()

    count = 0
    total = 0

    for index in range(n):
        if total + arr[index] <= c:
            total += arr[index]
            count += 1
        else:
            break
    
    print(count)
    
    t -= 1