from collections import Counter


t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    current_grannies = 1
    count = 0

    for index, value in enumerate(arr):
        if current_grannies >= value:
            count = index + 1
        current_grannies += 1
    
    print(count + 1)
        
    t -= 1
