from collections import Counter

t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    counter = Counter(arr)
    value = -1

    for key in counter:
        if counter[key] >= 3:
            value = key
            break
    
    print(value)

    t -= 1