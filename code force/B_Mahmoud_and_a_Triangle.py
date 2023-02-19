n = int(input())
arr = list(map(int, input().split()))
arr.sort()

is_possible = False

for index in range(2, n):
    if arr[index - 2] + arr[index -  1] > arr[index]:
        is_possible = True
        break

print("YES" if is_possible else "NO")