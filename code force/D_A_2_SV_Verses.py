from bisect import bisect_right

n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

for index in range(1, n):
    arr[index] += arr[index - 1]
    
result = 0
for index in range(n + 1):
    x = bisect_right(arr, (arr[index - 1] if index else 0) + (a - 1))
    y = bisect_right(arr, (arr[index - 1] if index else 0) + b)

    result += (y - x)

print(result)

# # count <= b:
# less_b = 0
# left = 0
# total = 0

# for right in range(n):
#     # add
#     total += arr[right]

#     while total > b:
#         # remove
#         total -= arr[left]
#         left += 1
    
#     if total <= b:
#         less_b += (right - left + 1)

# # count <= a
# less_a = 0
# left = 0

# total = 0

# for right in range(n):
#     total += arr[right]

#     while total >= a:
#         total -= arr[left]
#         left += 1
    
#     if total < a:
#         less_a += (right - left + 1)



    






    
    
    