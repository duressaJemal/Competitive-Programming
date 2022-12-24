# Link: https://codeforces.com/gym/418150/problem/D
#Q: A2SVians

# Time: O(M*N)
# Space: O(M*N)

from collections import Counter

n = int(input())
members = list(input().split())
flagged_members = set(input().split())

count = 0
for i in range(len(members)):
    is_valid = True
    counter = Counter(members[i])
    for key in counter:
        if counter[key] > 1:
            is_valid = False
            break
    
    if is_valid and members[i] not in flagged_members:
        count += 1

print(count)

