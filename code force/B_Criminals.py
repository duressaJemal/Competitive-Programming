def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0

    left = 0
    for right in range(n):
        # add
        if arr[right] == 0:
            if arr[left] == 0:
                left += 1
            else:
                arr[left] -= 1
                arr[right] += 1
                count += 1
                if not arr[left]:
                    left += 1      
        else:
            continue


    count += (sum(arr) - arr[-1])
    print(count)
    return 


t = int(input())
while t:

    solve()
    t -= 1