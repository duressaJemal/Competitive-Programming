n = int(input())
arr = list(map(int, input().split()))
output = []

for index in range(n):
    current = arr[index]
    s_index = index

    for i in range(index, n):
        if arr[i] < current:
            s_index = i
            current = arr[s_index]
    
    if s_index != index:
        output.append((index, s_index))
        arr[index], arr[s_index] = arr[s_index], arr[index]

print(len(output))
for x, y in output:
    print(x, y)
    

            
