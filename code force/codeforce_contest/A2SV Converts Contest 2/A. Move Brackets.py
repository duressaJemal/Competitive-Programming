n = int(input())
arr = []

for i in range(n):
    size = int(input())
    string = input()
    arr.append((size, string))


for pair in arr:
    size = pair[0]
    string = pair[1]

    