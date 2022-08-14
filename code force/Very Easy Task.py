# Link: https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/C

n, x, y = map(int, input().split())

def is_good(time):
    count = 0
    count += ((time//min(x, y)) + (((time - min(x, y))) // max(x, y)))
    if count >= n:
        return True
    return False

left = 0 # assume first bad value
right = 10e8 + 10 # first good value

while right > left + 1:
    mid = (left + right) // 2
    if is_good(mid):
        right = mid 
    else:
        left = mid 

print(int(right))
