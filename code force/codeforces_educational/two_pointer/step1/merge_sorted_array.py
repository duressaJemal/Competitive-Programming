a=[1,3,5,8,10]
b=[2,6,7,9,13]
c = [0] * (len(a) + len(b))

# would produce index out of range error
# i, j = 0, 0
# while i < len(a) or j < len(b):
#     if a[i] < b[j]:
#         c[i + j] = a[i]
#         i += 1
#     else:
#         c[i + j] = b[j]
#         j += 1
    
# Solution 1
# Add infinity to both the arrays
# a.append(float("inf"))
# b.append(float("inf"))

# i, j = 0, 0
# while i < len(a) - 1 or j < len(b) - 1:
#     if a[i] < b[j]:
#         print("if", i, j)
#         c[i + j] = a[i]
#         i += 1
#     else:
#         print("else", i, j)
#         c[i + j] = b[j]
#         j += 1
# print(c)

# Solution 2
# write accurate logic
i, j = 0, 0
while i < len(a) or j < len(b):
    if j == len(b) or (i < len(a) and a[i] < b[i]):
        c[i + j] = a[i]
        i += 1
    else:
        c[i + j] = b[j]
        j += 1
print(c)