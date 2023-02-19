# Link: https://codeforces.com/gym/419351/problem/D
#Q: Pattern

# Time: O(M*N) where M = len(patterns)
# Space: O(N + M) 

from collections import Counter

n = int(input())

arr = [0] * n
for i in range(n):
    arr[i] = input()

output = [0] * len(arr[0])

for i in range(len(arr[0])):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    
    counter = Counter(temp)

    if len(counter) > 2:
        output[i] = "?"
    elif len(counter) == 2:
        keys = list(counter.keys())
        if keys[0] == "?":
            output[i] = keys[1]
        elif keys[1] == "?":
            output[i] = keys[0]
        else:
            output[i] = "?"
    else:
        keys = list(counter.keys())
        if "?" == keys[0]:
            output[i] = "a"
        else:
            output[i] = keys[0]

print("".join(output))

        