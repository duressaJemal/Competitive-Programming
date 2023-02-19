t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))
    output = []

    left = 0
    right = n - 1

    while left <= right:
        output.append(arr[left])
        if left != right:
            output.append(arr[right])

        left += 1
        right -= 1
    
    print(*output)


    t -= 1