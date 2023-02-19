t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    current = arr[0]

    is_valid = True
    for num in arr:
        if num - current <= 1:
            current = num
        else:
            is_valid = False
            break
    
    print("YES" if is_valid else "NO")

    t -= 1