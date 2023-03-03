def solve():
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    is_valid = True

    gcd = float("inf")
    
    for f_index in range(n):
        for s_index in range(n):
            gcd = min(gcd, find_gcd(arr[f_index], arr[s_index]))

    if gcd <= 2:
        print("Yes")
    else:
        print("No")
    return

t = int(input())

while t:

    solve()
    t -= 1