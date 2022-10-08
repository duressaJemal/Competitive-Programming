# Link: https://codeforces.com/problemset/problem/1646/B
#Q: Quality vs Quantity

# Two pointers
# Time: O(N)
# Space: O(1)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    sum_l, sum_r, is_found = a[0], 0, False

    for i in range(1, n):
        sum_l += a[i]
        sum_r += a[n - i]
        if sum_r > sum_l:
            is_found = True
    
    print("YES" if is_found else "NO")



    
