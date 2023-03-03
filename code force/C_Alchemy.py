n = int(input())
arr = list(map(int, input().split()))

# l to r
edward = 0

# r to l
alphonso = 0

left = 0
right = n - 1

edward = 0
alphonso = 0

for t in range(1, 1001):
    if left <= right:
        if left == right and edward == alphonso:
            break
        if edward + arr[left] <= t:
            edward += arr[left]
            left += 1
        
        if alphonso + arr[right] <= t:
            alphonso += arr[right]
            right -= 1
    else:
        break

print(left, n - (right + 1))
    
