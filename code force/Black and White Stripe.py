# Link: https://codeforces.com/problemset/problem/1690/D
#Q: Black and White Stripe

# Time: O(N)
# Space: O(1)

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = input()

    counter = {"W": 0, "B": 0}
    l, res = 0, float("inf")
    for r in range(n):
        counter[arr[r]] += 1
        if r - l + 1 == k:
            res = min(res, counter["W"])
            counter[arr[l]] -= 1
            l += 1
    print(res)
