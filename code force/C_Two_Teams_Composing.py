from collections import Counter


t = int(input())
while t:

    n = int(input())
    counter = Counter(map(int, input().split()))

    max_count = 0
    for key in counter:
        max_count = max(max_count, counter[key])
    
    result = max(min(len(counter), max_count - 1), min(len(counter) - 1, max_count))
    print(result)
    t -= 1