# Link: https://codeforces.com/contest/1343/problem/C
#Q: C. Alternating Subsequence

# Time: O(N)
# Space: O(1)

t = int(input())
while t:

    n = int(input())
    arr = list(map(int, input().split()))
    output = 0

    left = 0
    while left < n:
        current = arr[left]
        right = left

        while right < n and arr[left] * arr[right] > 0:
            current = max(current, arr[right])
            right += 1
        
        output += current
        left = right
    
    print(output)

    t -= 1



# t = int(input())
# while t:

#     n = int(input())
#     arr = list(map(int, input().split()))
#     output = 0

#     current_index = 0

#     while current_index < n:
#         max_value = arr[current_index]
#         if arr[current_index] > 0:
#             while current_index < n and arr[current_index] > 0:
#                 max_value = max(max_value, arr[current_index])
#                 current_index += 1
#         else:
#             while current_index < n and arr[current_index] < 0:
#                 max_value = max(max_value, arr[current_index])
#                 current_index += 1
#         output += max_value
    
#     print(output)

#     t -= 1
