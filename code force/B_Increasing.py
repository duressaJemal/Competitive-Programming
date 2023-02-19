t = int(input())

while t:

    n = int(input())

    arr = list(map(int, input().split()))
    arr.sort()

    is_valid = True
    for index in range(1, n):
        if arr[index] == arr[index - 1]:
            is_valid = False
            break

    print("YES" if is_valid else "NO")
    

    t -= 1