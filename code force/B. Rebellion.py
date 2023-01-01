# Link: https://codeforces.com/problemset/problem/1746/B
#Q: B. Rebellion

# Time: O(N)
# Space: O(N)

t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    stack = []

    for index, value in enumerate(array):
        if value == 0:
            stack.append(index)
    
    count = 0
    
    for i in range(n):
        if array[i] == 1 and stack and stack[-1] > i:
            array[stack[-1]] = 1
            stack.pop()
            count += 1

            if not stack:
                break

    print(count)
    
t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    count = 0
    zeros_index = n - 1

    for index in range(n):
        if array[index] == 1:
            # find zeros current index
            while zeros_index > index and array[zeros_index] != 0:
                zeros_index -= 1
            
            if zeros_index > index:
                array[zeros_index] = 1
                zeros_index -= 1
                count += 1
            else:
                break

    print(count)
