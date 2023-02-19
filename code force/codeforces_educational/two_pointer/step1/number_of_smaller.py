# Two pointers

# O(size(a) + size(b))

# a=[1,3,5,8,10]
# b=[2,6,7,9,13]
# res = [0] * len(b)

# i, j = 0, 0
# while i < len(a) or j < len(b):
#     if j == len(b) or (i < len(a) and a[i] < b[j]):
#         i += 1
#     else:
#         res[j] = i 
#         j += 1
# print(res)

# Binary search

# O(size(b) * log(size(a)))
a = [1,3,5,8,10]
b = [2,6,7,9,13]
res = [0] * len(b)

for i in range(len(b)):
    left = -1 # assume good value
    right = len(b) # assume bad value
    while left + 1 < right:
        mid = (left + right) // 2
        if a[mid] < b[i]:
            left = mid
        else:
            right = mid
    print(left)
    res[i] = left + 1

print(res)

