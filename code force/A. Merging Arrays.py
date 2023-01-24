# Link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A
#Q: A. Merging Arrays

# Time: O(M + N)
# Space: O(M + N)

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [0] * (n + m)

len_a = 0
len_b = 0

while len_a < n or len_b < m:

    if len_b == m or (len_a < n and A[len_a] <= B[len_b]):
        C[len_a + len_b] = A[len_a]
        len_a += 1
    else:
        C[len_a + len_b] = B[len_b]
        len_b += 1

print(*C)
