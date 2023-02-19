t = int(input())

while t:

    arr = input()
    output = []

    n = len(arr)
    
    current_index = 0
    while current_index < n:
        curr = arr[current_index]
        left = current_index

        while current_index < n and arr[current_index] == curr:
            current_index += 1
        
        if (current_index - left) % 2 != 0:
            output.append(curr)
    
    output.sort()
    unique = set()
    res = []

    for num in output:
        if num not in unique:
            res.append(num)
            unique.add(num)
    print("".join(res))
    
    t -= 1

