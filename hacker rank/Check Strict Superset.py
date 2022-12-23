# Enter your code here. Read input from STDIN. Print output to STDOUT
# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=false
#Q: Check Strict Superset

super_set = set(input().split())
n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = set(input().split())

is_valid = True
for sets in arr:
    is_valid = is_valid and sets.issubset(super_set)

print(is_valid)
