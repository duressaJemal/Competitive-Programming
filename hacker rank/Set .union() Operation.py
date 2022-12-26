# Link: https://www.hackerrank.com/challenges/py-set-union/problem
#Q: Set .union() Operation

# Time: O(M + N)
# Space: O(M + N)

n_e = int(input())
english = set(map(int, input().split()))
n_f = int(input())
print(len(english.union(set(map(int, input().split())))))
