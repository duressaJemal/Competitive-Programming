n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
max_len = 0

for right in range(n):
    # add
    curr_sum += arr[right]

    # validate
    while curr_sum > s:

        # remove
        curr_sum -= arr[left]
        left += 1
    
    # record
    max_len = max(max_len, right - left + 1)

print(max_len)
