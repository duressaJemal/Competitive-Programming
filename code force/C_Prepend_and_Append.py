t = int(input())

while t:

    n = int(input())
    arr = input()

    left = 0
    right = n - 1

    while left <= right:
        if left != right:
            if int(arr[left]) + int(arr[right]) == 1:
                left += 1
                right -= 1
            else:
                break
        else:
            break

    print(right - left + 1)


    t -= 1