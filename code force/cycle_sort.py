def cycle_sort(arr):

    n = len(arr)

    for cur in range(n):
        while arr[cur] != cur + 1:
            
            temp = arr[cur]
            arr[cur] = arr[arr[cur] - 1]
            arr[temp - 1] = temp

    return arr

print(cycle_sort([3, 4, 2, 1, 5]))

