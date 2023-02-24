n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
result = 0

for right in range(n):

    # add
    curr_sum += arr[right]

    while curr_sum > s:
        # remove
        curr_sum -= arr[left]
        left += 1
    
    n = right - left + 1
    result += (n * (n + 1) // 2)

print(result)