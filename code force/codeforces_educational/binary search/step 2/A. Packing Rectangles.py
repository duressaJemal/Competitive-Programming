w, h, n = map(int, input().split())

def is_good(x):
    if (x // w) * (x // h) >= n:
        return True
    return False

left = 0 # bad rectangle side
right = 1 # good recangle side length
while not is_good(right): right *= 2

while right > left + 1:
    mid = (left + right) // 2
    if is_good(mid):
        right = mid
    else:
        left = mid

print(right)





