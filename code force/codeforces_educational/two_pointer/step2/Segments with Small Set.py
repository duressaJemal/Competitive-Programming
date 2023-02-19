# Link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/E
#Q: Segments with Small Set

# Two pointer

# Time: O(N)
# Space: O(N)

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# counter, distinct, res = {}, 0, 0

# l = 0
# for r in range(n):
#     # add
#     if arr[r] in counter:
#         counter[arr[r]] += 1
#     else:
#         counter[arr[r]] = 1

#     if counter[arr[r]] == 1:
#         distinct += 1

#     while distinct > k:
#         # remove
#         counter[arr[l]] -= 1
#         if counter[arr[l]] == 0:
#             distinct -= 1
#         l += 1
    
#     res += r - l + 1

        
# print(res)

# Or

n, k = map(int, input().split())
arr = list(map(int, input().split()))

counter = [0] * 100001
distinct = 0


def add(x):
    global distinct
    counter[x] += 1
    if counter[arr[r]] == 1:
        distinct += 1

def remove(x):
    global distinct
    counter[x] -= 1
    if counter[x] == 0: 
        distinct -= 1

def good():
    return distinct <= k

res, l = 0, 0
for r in range(n):
    add(arr[r])
    while not good():
        remove(arr[l])
        l += 1
    res += r - l + 1

print(res)