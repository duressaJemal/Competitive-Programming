from collections import Counter, defaultdict

n = int(input())

arr = list(map(int, input().split()))
dic = {1: [], 2: [], 3: []}

for index, value in enumerate(arr):
    dic[value].append(index + 1)

minimum = 5000
for value in dic.values():
    minimum = min(minimum, len(value))

print(minimum)

for operation in range(minimum):
    output = []
    for key in dic:
        output.append(dic[key][operation])
    print(*output)