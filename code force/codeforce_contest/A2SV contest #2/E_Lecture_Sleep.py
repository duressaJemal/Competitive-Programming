# Link: https://codeforces.com/gym/419351/problem/E
#Q: E_Lecture_Sleep

# Time: O(N)
# Space: O(1)

n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

total = 0
output = 0

left = 0
for right in range(n):
    # add
    if t[right] == 0:
        total += a[right]

    # check is good
    while right - left  + 1 > k:
        # remove
        if t[left] == 0:
            total -= a[left]
        left += 1

    output = max(total, output)

res = 0
for i in range(n):
    if t[i] == 1:
        res += a[i]

print(output + res)


    