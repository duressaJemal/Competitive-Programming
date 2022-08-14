# Link: https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/B


n , k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

def number_of_cuts(x):
    size = 0
    for i in range(n):
        size += (arr[i]//x)

    if size >= k:
        return True
    return False

left = 0.0 # always good
right = 10**8

for i in range(100):

    mid = (left + right) // 2
    if number_of_cuts(mid):
        left = mid
    else:
        right = mid

print(left)
