# Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B
#Q: B. Number of Smaller

# Time: O(M + N)
# Space: O(M)

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

output = []

current_index = 0

for index in range(m):

    while current_index < n and arr1[current_index] < arr2[index]:
        current_index += 1
    output.append(current_index)

print(*output)


