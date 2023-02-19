# Link: https://codeforces.com/problemset/problem/381/A
#Q: Sereja and Dima

n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n - 1
p_1, p_2, turn = 0, 0, 1
num = 0

while l <= r:

    if arr[l] > arr[r]:
        num = arr[l]
        l += 1
    else:
        num = arr[r]
        r -= 1
    
    if turn:
        p_1 += num
        turn = 0
    else:
        p_2 += num
        turn = 1
    
print(p_1)
print(p_2)


