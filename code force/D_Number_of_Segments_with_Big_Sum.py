n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
curr_sum = 0
res = 0

for right in range(n):
    # add
    curr_sum += arr[right]

    # validate
    while curr_sum - arr[left] >= s: # means can be reduced even more
        curr_sum -= arr[left]
        left += 1
    
    if curr_sum >= s:
        res += (left + 1)

print(res)
