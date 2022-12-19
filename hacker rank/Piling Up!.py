# Link: https://www.hackerrank.com/challenges/piling-up/problem
#Q: Piling Up!

t = int(input())
for _ in range(t):
    # Time: O(N)
    # Space: O(1)
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    l, r = 0, n - 1
    current = float("inf")
    is_valid = True
    
    while l <= r:
        mx = 0
        if arr[l] >= arr[r]:
            mx = arr[l]
            l += 1
        else:
            mx = arr[r]
            r -= 1
        if mx > current:
            is_valid = False
            break
        current = mx
    print("Yes" if is_valid else "No")
