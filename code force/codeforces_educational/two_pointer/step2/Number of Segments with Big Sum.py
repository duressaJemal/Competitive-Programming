# Link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D
#Q: Number of Segments with Big Sum

# Two pointers
# Time: O(N)
# Space: O(1)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, x, res = 0, 0, 0

for r in range(n):
    x += arr[r]
    while x - arr[l] >= s:
        x -= arr[l]
        l += 1
    
    if x >= s:
        res += l + 1

print(res)

    
# Or

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, x, res = 0, 0, 0

for r in range(n):
    x += arr[r]
    while x  >= s:
        x -= arr[l]
        l += 1
    
    res += l

print(res)