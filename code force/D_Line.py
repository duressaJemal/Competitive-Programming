t = int(input())

while t:

    n = int(input())
    arr = input()
    max_value = 0

    output = []
    diff = []

    for index in range(n):

        left = index
        right = n - (index + 1)

        # calculate diff
        if arr[index] == "L":
            max_value += left
            diff.append(abs(left - max(left, right)))
        else:
            max_value += right
            diff.append(abs(right - max(left, right)))
        
    diff.sort()

    for index in range(n - 1, -1, -1):
        max_value += diff[index]
        output.append(max_value)
    
    print(*output)
    t -= 1