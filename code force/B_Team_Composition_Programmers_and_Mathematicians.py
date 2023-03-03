def solve():
    a, b = map(int, input().split())

    def check(num):

        if min(a, b) < (num * 1):
            return False
        else:
            return (a + b) >= (4 * num)


    left = 0 # assume valid
    right = ((a + b) // 4) + 1

    while left + 1 < right:

        mid = left + (right - left) // 2

        if check(mid):
            left = mid
        else:
            right = mid
    
    print(left)
    return

t = int(input())
while t:
    solve()
    t -= 1