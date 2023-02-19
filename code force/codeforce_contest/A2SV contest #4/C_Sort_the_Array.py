n = int(input())
arr = list(map(int, input().split()))

count = []

for index in range(1, n):
    if arr[index] < arr[index - 1]:
        start = index - 1

        end = index
        for i in range(index + 1, n):
            if arr[i] <= arr[i - 1]:
                end += 1
            else:
                break
        count.append((start, end))
        break

if count:
    start = count[0][0]
    end = count[0][1]

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    is_valid = False
    if arr == sorted(arr):
        print("yes")
        print(count[0][0] + 1, count[0][1] + 1)
    else:
        print("no")
else:
    print("yes")
    print("1 1")