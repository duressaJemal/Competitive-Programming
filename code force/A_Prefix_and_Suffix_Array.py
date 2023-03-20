from collections import defaultdict

def solve():
    n = int(input())
    arr = list(input().split())

    def palindrome(arr):
        return arr[0] == arr[1][::-1]
    
    counter = defaultdict(list)

    for val in arr:
        counter[len(val)].append(val)
    
    is_valid = True

    for key in counter:
        
        curr = palindrome(counter[key])
        if not curr:
            is_valid = False
            break

    if is_valid:
        print("YES")
    else:
        print("NO")


t = int(input())
while t:
    solve()
    t -= 1