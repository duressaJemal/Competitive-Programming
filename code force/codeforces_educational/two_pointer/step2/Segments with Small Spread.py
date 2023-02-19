# Link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F
#Q: Segments with Small Spread

# Two pointers
# Time: O(N) -- Not Sure
# Space: O(N)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s1, s2 = [], []
max_s1, max_s2, min_s1, min_s2 = [float("-inf")], [float("-inf")], [float("inf")], [float("inf")]

res = 0

def add(x):
    s2.append(x)
    max_s2.append(max(max_s2[-1], s2[-1]))
    min_s2.append(min(min_s2[-1], s2[-1]))

    
def remove():
    if not s1:
        while s2:
            s1.append(s2.pop())
            max_s2.pop()
            min_s2.pop()
            max_s1.append(max(max_s1[-1], s1[-1]))
            min_s1.append(min(min_s1[-1], s1[-1]))
    s1.pop()
    max_s1.pop()
    min_s1.pop()

def good():
    mx = max(max_s1[-1], max_s2[-1])
    mn = min(min_s1[-1], min_s2[-1])

    return (mx - mn) <= k

l = 0
for r in range(n):
    add(arr[r])
    while not good():
        remove()
        l += 1
    res += r - l + 1

print(res)