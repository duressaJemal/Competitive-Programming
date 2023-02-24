n, p = map(int, input().split())
arr = list(map(int, input().split()))

output_index = 0
min_len = float("inf")

total_sum = sum(arr)

curr_sum = 0
left = 0
right = 0

while left < n:

    if curr_sum < p:
        itr_num = (p - curr_sum) // total_sum
    
        # update
        curr_sum += (itr_num * total_sum)
        right += (itr_num * n)

    if (p - curr_sum ) % total_sum:
        while curr_sum < p:
            curr_sum += arr[right % n]
            right += 1
    
    # record
    curr_length = right - left

    if curr_length < min_len:
        output_index = left
        min_len = curr_length
    
    curr_sum -= arr[left]
    left += 1

print(output_index + 1, min_len)
