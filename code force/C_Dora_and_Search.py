# Time: O(N)
# Space: O(1)

def solve():

    n = int(input())
    arr = list(map(int, input().split()))

    left = 0
    right = n - 1

    mn = 1
    mx = n

    while left <= right:
        
        if arr[left] == mn:
            left += 1
            mn += 1
        elif arr[left] == mx:
            left += 1
            mx -= 1
        elif arr[right] == mn:
            right -= 1
            mn += 1
        elif arr[right] == mx:
            right -= 1
            mx -= 1
        else:
            break
    
    if left <= right:
        print(left + 1, right + 1)
        return
    else:
        print(-1)
        return


t = int(input())
while t:
    solve()
    t -= 1