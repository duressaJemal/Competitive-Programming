t = int(input())

while t:

    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    min_value = 10 ** 9
    total = 0

    for value in arr:

        if value < 0:
            count += 1
        
        pos = max(value, 0 - value)
        total += pos
        min_value = min(min_value, pos)
    

    if count % 2 == 0:
        print(total)
    else:
        print(total - 2 * min_value)

    t -= 1