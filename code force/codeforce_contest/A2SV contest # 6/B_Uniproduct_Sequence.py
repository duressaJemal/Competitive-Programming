n = int(input())
arr = list(map(int, input().split()))

current_value = 1
count = 0
count_zeros = 0

for value in arr:
    if value < 0:
        count += (0 - value - 1)
        current_value *= -1
    elif value > 0:
        count += (value - 1)
    else:
        count_zeros += 1

if current_value > 0:
    print(count + count_zeros)
else:
    if count_zeros:
        print(count + count_zeros)
    else:
        print(count + 2)


    

