# Link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/C
#Q: Number of Segments with Small Sum

# Two pointers
# Time: O(N)
# Space: O(1)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, x, res = 0, 0, 0

for r in range(n):
    x += arr[r]
    while x > s:
        x -= arr[l]
        l += 1
    
    res += r - l + 1

print(res)
    
    

