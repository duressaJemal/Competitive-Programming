import sys 
input = lambda:sys.stdin.readline().strip()

t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))

    is_valid = False

    for index in range(1, len(arr)):
        if arr[index] >= arr[index - 1]:
            is_valid = True
            break
    
    print("YES" if is_valid else "NO")

    t -= 1
