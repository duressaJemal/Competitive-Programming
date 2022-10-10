# Link: https://codeforces.com/problemset/problem/1462/A
#Q: Favorite Sequence

# Two pointer

# Time: O(N)
# Space: O(N)

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    output = []

    l, r = 0, n - 1
    while l <= r:
        output.append(b[l])
        if l != r:
            output.append(b[r])
        l += 1
        r -= 1


    for num in output:
        print(num)


#

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    output = [0] * n

    l, r = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            output[i] = b[l]
            l += 1
        else:
            output[i] = b[r]
            r -= 1

    for num in output:
        print(num)
