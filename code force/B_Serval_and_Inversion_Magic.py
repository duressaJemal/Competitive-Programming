def solve():
    n = int(input())
    arr = list(map(int, input()))

    left = 0
    right = n - 1

    prev_count = 0
    t_count = []

    is_possible = True
    count = 0
    while left <= right:
        count += 1
        if arr[left] != arr[right]:
            t_count.append(count)
        left += 1
        right -= 1
    

    for index in range(1, len(t_count)):
        if t_count[index] - t_count[index - 1] > 1:
            is_possible = False
            break
        
    print("Yes" if is_possible else "No")
    return


t = int(input())
while t:

    solve()
    t -= 1


