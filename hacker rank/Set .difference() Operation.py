# Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=false
#Q: Set .difference() Operation

# Time: O(N + M)
# Space: O(N + M)

n_e = int(input())
english = set(map(int, input().split()))
n_f = int(input())
french = set(map(int, input().split()))

count = 0
for key in english:
    if key not in french:
        count += 1

print(count)
