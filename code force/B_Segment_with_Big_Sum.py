n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
min_len = float("inf")

for right in range(n):
    # add
    curr_sum += arr[right]

    # validate
    while curr_sum - arr[left] >= s: # can be reduced even more

        # remove
        curr_sum -= arr[left]
        left += 1
    
    # record
    if curr_sum >= s:
        min_len = min(min_len, right - left + 1)

print(-1 if min_len == float("inf") else min_len)
