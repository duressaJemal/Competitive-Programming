# Link: https://codeforces.com/problemset/problem/1744/A
#Q: Number Replacement

# Time: O(N)
# Space: O(N)

t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    string = list(input())

    counter = {}
    is_valid = True

    for i in range(n):
        if arr[i] in counter:
            if counter[arr[i]] != string[i]:
                is_valid = False
                break
        else:
            counter[arr[i]] = string[i]
    print("YES" if is_valid else "NO")
    


